from django.db import models

# Create your models here.


class Article(models.Model):
    folder = '/tmp/testFile'
    img = models.FileField(null=True, blank=True, upload_to=folder)
    title = models.CharField(null=True, blank=True, max_length=20)
    content = models.TextField(null=True, blank=True)
    views = models.IntegerField(null=True, blank=True)
    likes = models.IntegerField(null=True, blank=True)
    createtime = models.DateField(auto_now=False, auto_now_add=False)
    tag = models.CharField(null=True, blank=True, max_length=5)
