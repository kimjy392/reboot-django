from django.db import models

# Create your models here.

class Reporter(models.Model):
    name = models.CharField(max_length=20)

class Article(models.Model):
    title = models.CharField(max_length=50)
    content = models.TextField()
    image = models.ImageField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    # reporter = models.ForeignKey(Reporter, on_delete=models.CASCADE)


class Comment(models.Model):
    content = models.CharField(max_length=50)
    article = models.ForeignKey(Article, on_delete=models.CASCADE)