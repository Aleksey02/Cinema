# Generated by Django 4.0.4 on 2022-07-20 07:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0007_alter_film_title'),
    ]

    operations = [
        migrations.AlterField(
            model_name='film',
            name='lim_age',
            field=models.CharField(choices=[('3', '3+'), ('6', '6+'), ('12', '12+'), ('16', '16+'), ('18', '18+')], default='3', max_length=50, verbose_name='Возрастной рейтинг'),
        ),
        migrations.AlterField(
            model_name='film',
            name='tipe_film',
            field=models.CharField(choices=[('movie', 'Фильм'), ('tv-series', 'Сериал'), ('carton', 'Мультфильм')], default='film', max_length=50, verbose_name='Тип фильма'),
        ),
    ]
