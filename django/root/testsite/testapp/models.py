from django.db import models

# Create your models here.


class Person(models.Model):
    name = models.CharField(null=True, blank=True, max_length=200)
    job = models.CharField(null=True, blank=True, max_length=200)

    def __str__(self):
        return self.name


class Article(models.Model):
    headline = models.CharField(null=True, blank=True, max_length=200)
    text = models.TextField(null=True, blank=True)

    def __str__(self):
        return self.headline
