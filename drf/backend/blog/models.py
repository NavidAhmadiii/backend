from django.contrib.auth.models import User
from django.utils import timezone
from django.db import models


# Create your models here.


class Article(models.Model):
    title = models.CharField(max_length=250)
    slug = models.SlugField()
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    content = models.TextField()
    publish = models.DateTimeField(default=timezone.now)
    created = models.DateTimeField(auto_now_add=True)  # when object created save the time now
    updated = models.DateTimeField(auto_now=True)  # when object updated save the time
    status = models.BooleanField(default=False)

    def __str__(self):
        return self.title
