# Generated by Django 3.1.13 on 2021-10-04 06:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('vocabulary', '0005_vocabulary_searched_datetime'),
    ]

    operations = [
        migrations.AlterField(
            model_name='vocabulary',
            name='created_datetime',
            field=models.DateTimeField(auto_now_add=True),
        ),
    ]
