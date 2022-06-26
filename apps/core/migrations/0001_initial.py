# Generated by Django 4.0.4 on 2022-06-26 15:33

from django.db import migrations, models
import django.db.models.deletion
import multiselectfield.db.fields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Actor',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('full_name', models.CharField(max_length=50, verbose_name='name')),
            ],
        ),
        migrations.CreateModel(
            name='Director',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('full_name', models.CharField(max_length=50, verbose_name='name')),
            ],
        ),
        migrations.CreateModel(
            name='Film',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200, verbose_name='Название')),
                ('description', models.TextField(verbose_name='Описание')),
                ('ganre', multiselectfield.db.fields.MultiSelectField(choices=[('1', 'Боевик'), ('2', 'Комедия'), ('3', 'Триллер'), ('4', 'Ужасы'), ('5', 'Детектив'), ('6', 'Драма'), ('7', 'Фэнтези'), ('8', 'Фантастика'), ('9', 'Приключения'), ('10', 'Криминал')], max_length=25, verbose_name='Жанр')),
                ('tipe_film', models.CharField(choices=[('film', 'Фильм'), ('serial', 'Сериал'), ('multfilm', 'Мультфильм')], default='1_type', max_length=50, verbose_name='Тип фильма')),
                ('year', models.IntegerField(verbose_name='Год выпуска')),
                ('image', models.ImageField(null=True, upload_to='', verbose_name='Картинка')),
                ('lim_age', models.CharField(choices=[('1', '3+'), ('2', '12+'), ('3', '16+'), ('4', '18+')], default='1', max_length=50, verbose_name='Возрастной рейтинг')),
                ('country', models.CharField(blank=True, max_length=50, null=True, verbose_name='Страна')),
                ('video', models.FileField(null=True, upload_to='videos_uploaded')),
                ('actor', models.ManyToManyField(related_name='actor', to='core.actor')),
                ('director', models.ManyToManyField(related_name='director', to='core.director')),
            ],
        ),
        migrations.CreateModel(
            name='New',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50, verbose_name='Заголовок')),
                ('description', models.TextField(verbose_name='Текст')),
            ],
        ),
        migrations.CreateModel(
            name='Poster',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='', verbose_name='слайд 1')),
                ('title', models.CharField(max_length=50, verbose_name='название слайда')),
                ('film', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='film', to='core.film')),
            ],
        ),
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('comment_text', models.TextField(verbose_name='Текст комментария')),
                ('comment_author', models.CharField(max_length=50, verbose_name='Имя автора комментария')),
                ('date_create', models.DateField(auto_now_add=True, null=True)),
                ('film', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='comments', to='core.film')),
            ],
        ),
    ]