from celery import shared_task, signals
from django.utils import timezone
import requests
from bs4 import BeautifulSoup
from urllib.parse import urljoin
from .models import World, Sports, Trade
from celery.signals import task_success

def fetch_and_parse_url(session, url):
    response = session.get(url)
    response.raise_for_status()
    return BeautifulSoup(response.text, 'html.parser')

def extract_article_details(soup):
    title_box = soup.find('div', class_="details-title")
    brief_box = soup.find('div', class_="details-brief")
    
    title = title_box.find('h1').text.strip() if title_box and title_box.find('h1') else "No Title"
    paragraphs = [p.text.strip() for p in brief_box.find_all('p')] if brief_box else []
    content = "\n".join(paragraphs)
    
    return title, content

def save_article(model, title, content):
    if not model.objects.filter(title=title).exists():
        model.objects.create(title=title, content=content, date=timezone.now())

@shared_task
def scrape_news(base_url, model):
    url = f'{base_url}/'

    try:
        with requests.Session() as session:
            soup = fetch_and_parse_url(session, url)
            all_links = soup.find_all('a')

            links_list = [urljoin(url, link.get('href')).strip() for link in all_links if link.get('href') and link.get('href').startswith(base_url)]
            unique_list = list(set(links_list))

            for link in unique_list:
                try:
                    article_soup = fetch_and_parse_url(session, link)
                    title, content = extract_article_details(article_soup)
                    save_article(model, title, content)
                except Exception as e:
                    print(f"Error fetching data from {link}: {e}")
    except Exception as e:
        print(f"Error connecting to {url}: {e}")

@shared_task
def scrape_world_news():
    scrape_news('https://bangla.bdnews24.com/world', World)

@shared_task
def scrape_sports_news():
    scrape_news('https://bangla.bdnews24.com/sport', Sports)

@shared_task
def scrape_trade_news():
    scrape_news('https://bangla.bdnews24.com/business', Trade)

@shared_task
def refresh_data():
    urls = [
        'http://127.0.0.1:8000/sports/',
        'http://127.0.0.1:8000/trade/',
        'http://127.0.0.1:8000/world/'
    ]
    
    for url in urls:
        try:
            response = requests.get(url)
            response.raise_for_status()  # Raise an error for bad status codes
            print(f"Successfully refreshed {url}")
        except requests.RequestException as e:
            print(f"Error refreshing {url}: {e}")

@task_success.connect
def on_task_success(sender=None, headers=None, body=None, **kwargs):
    if sender.name in ['news.tasks.scrape_world_news', 'news.tasks.scrape_sports_news', 'news.tasks.scrape_trade_news']:
        refresh_data.delay()
