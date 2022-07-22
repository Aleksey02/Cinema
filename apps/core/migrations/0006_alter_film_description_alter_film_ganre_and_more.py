# Generated by Django 4.0.4 on 2022-07-19 18:42

from django.db import migrations, models
import multiselectfield.db.fields


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0005_alter_film_title'),
    ]

    operations = [
        migrations.AlterField(
            model_name='film',
            name='description',
            field=models.TextField(blank=True, null=True, verbose_name='Описание'),
        ),
        migrations.AlterField(
            model_name='film',
            name='ganre',
            field=multiselectfield.db.fields.MultiSelectField(choices=[('боевик', 'Боевик'), ('комедия', 'Комедия'), ('триллер', 'Триллер'), ('ужасы', 'Ужасы'), ('детектив', 'Детектив'), ('драма', 'Драма'), ('фэнтези', 'Фэнтези'), ('фантастика', 'Фантастика'), ('приключения', 'Приключения'), ('криминал', 'Криминал'), ('мелодрама', 'мелодрама')], default='комедия', max_length=25, verbose_name='Жанр'),
        ),
        migrations.AlterField(
            model_name='film',
            name='lim_age',
            field=models.CharField(choices=[('3', '3+'), ('12', '12+'), ('16', '16+'), ('18', '18+')], default='3', max_length=50, verbose_name='Возрастной рейтинг'),
        ),
        migrations.AlterField(
            model_name='film',
            name='year',
            field=models.IntegerField(blank=True, null=True, verbose_name='Год выпуска'),
        ),
    ]