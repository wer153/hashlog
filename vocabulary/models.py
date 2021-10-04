from django.db import models


class Vocabulary(models.Model):
    title = models.CharField(unique=True, max_length=100, db_index=True)
    subtitle = models.CharField(max_length=100, db_index=True)
    created_datetime = models.DateTimeField(auto_now_add=True)
    modified_datetime = models.DateTimeField(auto_now=True)
    content = models.TextField()

    def __str__(self):
        return f'{self.title}: {self.subtitle}'
