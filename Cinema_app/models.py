from django.db import models
from django.urls import reverse
from multiselectfield import MultiSelectField


# Create your models here.
class Film(models.Model):
    CHOICES = (
        ('1', 'Боевик'),
        ('2', 'Комедия'),
        ('3', 'Триллер'),
        ('4', 'Ужасы'),
    )
    CHOICES_film = (
        ('1_type', 'film'),
        ('2_type', 'serial'),
        ('3_type', 'mult'),
    )
    CHOICES_lim_age = (
        ('1', '3+'),
        ('2', '12+'),
        ('3', '16+'),
        ('4', '18+'),
    )

    title = models.CharField(max_length=200, verbose_name='Название')
    description = models.TextField(verbose_name='Описание')
    ganre = MultiSelectField(verbose_name='Жанр', choices=CHOICES, max_length=5)
    tipe_film = models.CharField(verbose_name='Тип фильма', choices=CHOICES_film, max_length=50, default='1_type')
    year = models.IntegerField(verbose_name='Год выпуска')
    image = models.ImageField(verbose_name='Картинка', null=True)
    lim_age = models.CharField(verbose_name='Возрастной рейтинг', choices=CHOICES_lim_age, max_length=50, default='1')
    country = models.CharField(verbose_name='Страна', max_length=50, blank=True, null=True)
    poster = models.ImageField(verbose_name='Постер', null=True, blank=True)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('adminka')

class Comment(models.Model):
    film = models.ForeignKey(Film, on_delete=models.CASCADE, related_name='comments')
    comment_text = models.TextField(verbose_name='Текст комментария')
    comment_author = models.CharField(max_length=50, verbose_name='Имя автора комментария')

    def get_absolute_url(self):
        return reverse('film', kwargs={'pk': self.film_id})

    def __str__(self):
        return self.comment_author

class Actor(models.Model):
    full_name = models.CharField(max_length=50, verbose_name='name')
    film = models.ManyToManyField(Film)

    def __str__(self):
        return self.full_name

class Director(models.Model): #Режиссёр
    full_name = models.CharField(max_length=50, verbose_name='name')
    film = models.ManyToManyField(Film)

    def __str__(self):
        return self.full_name

class New(models.Model):
    title = models.CharField(max_length=50, verbose_name='Заголовок')
    description = models.TextField(verbose_name='Текст')

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('adminka')
