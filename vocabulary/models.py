from django.db import models


class Vocabulary(models.Model):
    title = models.CharField(max_length=100)
    subtitle = models.CharField(max_length=100)
    date = models.DateField(auto_now=True)
    text = models.TextField()

    def __str__(self):
        return f'{self.title}: {self.subtitle}'
