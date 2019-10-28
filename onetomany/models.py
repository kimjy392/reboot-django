from django.db import models

# Create your models here.

class User(models.Model):
    username = models.CharField(max_length=140)

class Article(models.Model):
    title = models.CharField(max_length=140)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

class Comment(models.Model):
    content = models.CharField(max_length=140)
    article = models.ForeignKey(Article, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

