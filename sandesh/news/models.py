from django.db import models
from django.contrib.auth.models import User
import sqlalchemy as sa

class World(models.Model):
    title=models.CharField(max_length=300)
    content=models.TextField()
    image=models.ImageField(upload_to="post/",blank=True,null=True)
    date=models.DateField(auto_now_add=True)
    def __str__(self):
        return self.title[:70]
    

class Sports(models.Model):
    title=models.CharField(max_length=300)
    content=models.TextField()
    image=models.ImageField(upload_to="post/",blank=True,null=True)
    date=models.DateField(auto_now_add=True)
    def __str__(self):
        return self.title[:70]
    
class Trade(models.Model):
    title=models.CharField(max_length=300)
    content=models.TextField()
    image=models.ImageField(upload_to="post/",blank=True,null=True)
    date=models.DateField(auto_now_add=True)
    def __str__(self):
        return self.title[:70]
    
class Profile(models.Model):
    user=models.OneToOneField(User,on_delete=models.CASCADE)
    image=models.ImageField(upload_to="profile/",default="default.jpg", blank=True,null=True)

    def __str__(self):
        return self.user.username
    