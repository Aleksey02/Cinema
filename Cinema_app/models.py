from django.db import models
from django.urls import reverse
from multiselectfield import MultiSelectField


# Create your models here.

class Actor(models.Model):
    full_name = models.CharField(max_length=50, verbose_name='name')

    def __str__(self):
        return self.full_name

class Director(models.Model): #Режиссёр
    full_name = models.CharField(max_length=50, verbose_name='name')

    def __str__(self):
        return self.full_name

class Film(models.Model):
    CHOICES = (
        ('1', 'Боевик'),
        ('2', 'Комедия'),
        ('3', 'Триллер'),
        ('4', 'Ужасы'),
        ('5','Детектив'),
        ('6','Драма'),
        ('7','Фэнтези'),
        ('8','Фантастика'),
        ('9','Приключения'),
        ('10','Криминал'),
    )
    CHOICES_film = (
        ('1_type', 'Фильм'),
        ('2_type', 'Сериал'),
        ('3_type', 'Мультфильм'),
    )
    CHOICES_lim_age = (
        ('1', '3+'),
        ('2', '12+'),
        ('3', '16+'),
        ('4', '18+'),
    )

    title = models.CharField(max_length=200, verbose_name='Название')
    description = models.TextField(verbose_name='Описание')
    ganre = MultiSelectField(verbose_name='Жанр', choices=CHOICES, max_length=25)
    tipe_film = models.CharField(verbose_name='Тип фильма', choices=CHOICES_film, max_length=50, default='1_type')
    year = models.IntegerField(verbose_name='Год выпуска')
    image = models.ImageField(verbose_name='Картинка', null=True)
    lim_age = models.CharField(verbose_name='Возрастной рейтинг', choices=CHOICES_lim_age, max_length=50, default='1')
    country = models.CharField(verbose_name='Страна', max_length=50, blank=True, null=True)
    video = models.FileField(upload_to='videos_uploaded', null=True)
    actor = models.ManyToManyField(Actor, related_name='actor')
    director = models.ManyToManyField(Director, related_name='director')

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('adminka')

class Comment(models.Model):
    film = models.ForeignKey(Film, on_delete=models.CASCADE, related_name='comments')
    comment_text = models.TextField(verbose_name='Текст комментария')
    comment_author = models.CharField(max_length=50, verbose_name='Имя автора комментария')
    date_create = models.DateField(auto_now_add=True, null=True)

    def get_absolute_url(self):
        return reverse('film', kwargs={'pk': self.film_id})

    def __str__(self):
        return self.comment_author





class New(models.Model):
    title = models.CharField(max_length=50, verbose_name='Заголовок')
    description = models.TextField(verbose_name='Текст')

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('adminka')

class Poster(models.Model):
    image = models.ImageField(verbose_name='слайд 1')
    title = models.CharField(verbose_name='название слайда', max_length=50)
    film = models.ForeignKey(Film, on_delete=models.CASCADE, related_name='film', null=True)

    def __str__(self):
        return self.title