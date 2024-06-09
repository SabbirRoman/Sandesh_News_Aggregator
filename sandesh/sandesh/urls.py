from django.contrib import admin
from django.urls import path, include, re_path
from django.views.generic import TemplateView
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path,include
from rest_framework import routers
from news.views import WorldView,SportsView,TradeView,WorldViewData,SportViewData,TradeViewData,ProfileView,RegisterView
from rest_framework.authtoken.views import obtain_auth_token

route=routers.DefaultRouter()
route.register("worldview",WorldViewData,basename="worldview")
route.register("sportview",SportViewData,basename="sportview")
route.register("tradeview",TradeViewData,basename="tradeview")


urlpatterns = [
    path('admin/', admin.site.urls),
    path('profile/',ProfileView.as_view(),name='profile'),
    path('world/',WorldView.as_view(), name='worldview'),
    path('sports/',SportsView.as_view(),name='sportsview'),
    path('trade/',TradeView.as_view(),name='tradeview'),
    path('api/',include(route.urls)),
    path('profile/',ProfileView.as_view()),
    path('login/',obtain_auth_token),
    path('register/',RegisterView.as_view())
 
]

urlpatterns += static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
urlpatterns += static(settings.STATIC_URL,document_root=settings.STATIC_ROOT)
