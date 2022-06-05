from django.contrib.auth.models import User
from django.db import models
from datetime import datetime

# Create your models here.
class Draft(models.Model):
    title = models.CharField(max_length=100,null=True,blank=True)
    body = models.CharField(max_length=1000000,null=True,blank=True)
    created_at = models.DateTimeField(default=datetime.now, blank=True)
    author = models.ForeignKey(User, null=True, blank=True,on_delete=models.CASCADE)


class Post(models.Model):
    post=models.ForeignKey(Draft,null=True,blank=True,on_delete=models.CASCADE)

    @property
    def post_id(self):
        return self.post.id