from django.db import models
from django.contrib.auth.models import User
from datetime import datetime
# Create your models here.
class Blog(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE,null=True,blank=True)
    title = models.CharField(max_length=60)
    author = models.CharField(max_length=60)
    content = models.TextField(max_length=600,null=True,blank=True)
    date = models.DateTimeField(auto_now_add=True,blank=True,null=True)

    def __str__(self):
        return self.title

    class Meta:
        order_with_respect_to = 'user'

