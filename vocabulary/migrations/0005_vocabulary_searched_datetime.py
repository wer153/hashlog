# Generated by Django 3.1.13 on 2021-10-04 05:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('vocabulary', '0004_auto_20210929_1237'),
    ]

    operations = [
        migrations.AddField(
            model_name='vocabulary',
            name='searched_datetime',
            field=models.DateTimeField(auto_now=True),
        ),
    ]
