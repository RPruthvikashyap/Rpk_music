from os import name
from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Song(models.Model):
    song_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=2000)
    singer = models.CharField(max_length=2000)
    tags = models.CharField(max_length=100)
    image = models.CharField(max_length=100000, default="")
    song = models.FileField(upload_to='images')
    movie = models.CharField(max_length=1000, default="")
    credit = models.CharField(max_length=100000, default="")

    def __str__(self):
        return self.name

class Watchlater(models.Model):
    watch_id = models.AutoField(primary_key=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    video_id = models.CharField(max_length=10000000, default="")

class History(models.Model):
    hist_id = models.AutoField(primary_key=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    music_id = models.CharField(max_length=10000000, default="")

class Channel(models.Model):
    channel_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=1000)
    music = models.CharField(max_length=100000000)

class Album(models.Model):
    Album_id = models.AutoField(primary_key=True)
    Album_name = models.CharField(max_length=2000)
    singer = models.CharField(max_length=2000)
    genre = models.CharField(max_length=100)
    image = models.CharField(max_length=100000, default="")
    movie = models.CharField(max_length=1000, default="")
    credit = models.CharField(max_length=100000, default="")
    name1 = models.CharField(max_length=2000)
    songa = models.FileField(upload_to='images')
    name2 = models.CharField(max_length=2000)
    songb = models.FileField(upload_to='images')
    name3 = models.CharField(max_length=2000)
    songc = models.FileField(upload_to='images')
    name4 = models.CharField(max_length=2000)
    songd = models.FileField(upload_to='images')
    name5 = models.CharField(max_length=2000)
    songe = models.FileField(upload_to='images')

    def __str__(self):
        return self.Album_name
    
