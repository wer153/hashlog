# Generated by Django 3.1.13 on 2021-09-29 12:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('vocabulary', '0002_auto_20210929_1235'),
    ]

    operations = [
        migrations.AlterField(
            model_name='vocabulary',
            name='subtitle',
            field=models.CharField(db_index=True, max_length=100),
        ),
        migrations.AlterField(
            model_name='vocabulary',
            name='title',
            field=models.CharField(db_index=True, max_length=100),
        ),
    ]
