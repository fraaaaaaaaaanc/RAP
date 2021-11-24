from django.db import models

# Create your models here.


class Rap(models.Model):
    title = models.CharField(max_length=255)
    content = models.TextField(blank=True)
    photo = models.ImageField(upload_to="photos/")
    time_create = models.DateTimeField(auto_now_add=True)
    time_update = models.DateTimeField(auto_now=True)
    is_published = models.BooleanField(default=True)


class RapArt(models.Model):
    name = models.CharField('Name', max_length=50)
    description = models.TextField('description')
    photo = models.ImageField('photo', upload_to="photos/")
    rating = models.SmallIntegerField('rating')
    data = models.DateTimeField('data')

