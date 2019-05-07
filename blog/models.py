from django.db import models
from django.utils import timezone


# Create your models here.
class Article(models.Model):
    title = models.CharField(max_length=20)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    published_at = models.DateTimeField()

    def __str__(self):
        return self.title

    def save_article(self):
        self.published_at = timezone.now()
        self.save()
