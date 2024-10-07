from django.db import models


# Create your models here.

class Post(models.Model):
    title = models.CharField(max_length=30)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)


class SavedPostNums(models.Model):
    number_of_posts = models.IntegerField(default=2)
