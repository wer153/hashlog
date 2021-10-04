from django.db import models


class Vocabulary(models.Model):
    created_datetime = models.DateTimeField(auto_now_add=True)
    modified_datetime = models.DateTimeField(auto_now=True)

    title = models.CharField(unique=True, max_length=100, db_index=True)
    subtitle = models.CharField(max_length=100, db_index=True)
    content = models.TextField()
    starred = models.BooleanField(default=False, db_index=True)

    def __str__(self):
        return f'{self.title}: {self.subtitle}'
