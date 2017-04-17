from django.db import models
from faker import Factory
import time

# Create your models here.
class Article(models.Model):
    title = models.CharField(max_length=500)
    img = models.CharField(max_length=250)
    content = models.TextField(null=True, blank=True)
    views = models.IntegerField(default=0)
    likes = models.IntegerField(default=0)
    # createtime = models.DateField()

    def __str__(self):
        return self.title

# f = '/static/images/default.jpg'
# fake = Factory.create()
# for i in range(40):
#     A = Article(
#         title = fake.text(max_nb_chars=50),
#         content = fake.text(max_nb_chars=500),
#         img = f,
#         # createtime = time.localtime()
#
#     )
#     A.save()
