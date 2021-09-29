from django.db import models


class Vocabulary(models.Model):
    title = models.CharField(max_length=100)
    subtitle = models.CharField(max_length=100)
    created_datetime = models.DateTimeField(auto_now=True)
    modified_datetime = models.DateTimeField(auto_now=True)
    content = models.TextField()

    def __str__(self):
        return f'{self.title}: {self.subtitle}'
