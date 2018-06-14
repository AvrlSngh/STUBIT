from django.db import models
from accounts.models import User


class MyNote(models.Model):
    title = models.CharField(max_length=100, null=False)
    slug = models.SlugField(null=False)
    body = models.TextField(null=False)
    date = models.DateTimeField(auto_now_add=True)
    author = models.ForeignKey(User, default=None, on_delete=models.CASCADE)

    def __str__(self):
        return self.title

    def snippet(self):
        return self.body[:50] + '...'
