from django.db import models
from faker import Factory
from django.contrib.auth.models import User

# Create your models here.
class Article(models.Model):
    title = models.CharField(max_length=500)
    img = models.CharField(max_length=250)
    content = models.TextField(null=True, blank=True)
    views = models.IntegerField(default=0)
    likes = models.IntegerField(default=0)
    createtime = models.DateField()

    def __str__(self):
        return self.title

class Comment(models.Model):
    name = models.CharField(max_length=500)
    avatar = models.CharField(max_length=250, default="static/images/default.png")
    comment = models.TextField(null=True, blank=True)
    createtime = models.DateField(auto_now=True)

    belong_to = models.ForeignKey(to=Article, related_name="under_comments", null=True, blank=True)

    def __str__(self):
        return self.name


class UserProfile(models.Model):
    belong_to = models.OneToOneField(to=User, related_name='profile', on_delete=None, to_field=None)
    profile_image = models.FileField(verbose_name=None, name=None, upload_to='profile_image', storage=None)

class Ticket(models.Model):
    voter = models.ForeignKey(to=UserProfile, on_delete=None, related_name='voted_tickets', related_query_name=None, limit_choices_to=None, parent_link=False, to_field=None, db_constraint=True)
    article = models.ForeignKey(to=Article, on_delete=None, related_name='tickets', related_query_name=None, limit_choices_to=None, parent_link=False, to_field=None, db_constraint=True)
    VOTE_CHOICES = (
        ('like', 'like'),
        ('dislike', 'dislike'),
        ('normal', 'normal'),
    )
    choice = models.CharField(choices=VOTE_CHOICES, max_length=10)

    def __str__(self):
        return str(self.id)
