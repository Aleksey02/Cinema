# Generated by Django 4.0.4 on 2022-07-19 18:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0006_alter_film_description_alter_film_ganre_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='film',
            name='title',
            field=models.CharField(max_length=200, verbose_name='Название'),
        ),
    ]