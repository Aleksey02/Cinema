# Generated by Django 4.0.4 on 2022-05-25 15:09

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Cinema_app', '0004_director'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='actor',
            name='image',
        ),
    ]