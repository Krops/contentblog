from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User

class Post(models.Model):
    time_post = models.DateTimeField(auto_now_add=True)
    time_edit = models.DateTimeField(auto_now=True)
    slug = models.SlugField(unique=True)
    theme = models.CharField(max_length=50)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    message = models.TextField()
    rate = models.IntegerField(default=0)
    parent_category = models.ForeignKey('self', null=True, blank=True, on_delete=False)

    def __str__(self):
        return self.slug

