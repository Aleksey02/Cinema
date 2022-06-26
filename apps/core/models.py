from django.db import models
from django.urls import reverse
from multiselectfield import MultiSelectField


# Create your models here.

class Actor(models.Model):
    """
    Модель Актёра, который учасвует в фильме.
    Имеются поля: full_name - полное имя актёра (Фамилия Имя)
    """
    full_name = models.CharField(max_length=50, verbose_name='name')

    def __str__(self):
        return self.full_name

class Director(models.Model): #Режиссёр
    """
    Модель Режиссёра, который учасвует в фильме.
    Имеются поля: full_name - полное имя режиссёра (Фамилия Имя)
    """
    full_name = models.CharField(max_length=50, verbose_name='name')

    def __str__(self):
        return self.full_name

class Film(models.Model):
    """
        Данная модель содержит в себе всю информацию о фильме и показывает это на сайте.
        Имеются поля: title - Название фильма, description - полное описание фильма,
        ganre - жанр данного фильма, tipe_film - Тип фильма(Фильм, сериал, мультфильм)
        year - год выпуска фильма, image - постер фильма,
        lim_age - возрастное ограничение фильма, country - страна выпуска фильма,
        video - видео запись фильма, actor - актёры которые участвовали в фильме
        director - режиссёры которые участвовали в фильме
        """
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
        ('film', 'Фильм'),
        ('serial', 'Сериал'),
        ('multfilm', 'Мультфильм'),
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
    """
    Модель комментариев, позволяет добвлять комментарии к фильму.
    Имеются поля: film - указывает к какому фильму будет относится комментарий
    comment_text - Текст комментрия который вводит пользователь
    comment_author - Имя автора комментария,
    date_create - Дата создания комментария
    """
    film = models.ForeignKey(Film, on_delete=models.CASCADE, related_name='comments')
    comment_text = models.TextField(verbose_name='Текст комментария')
    comment_author = models.CharField(max_length=50, verbose_name='Имя автора комментария')
    date_create = models.DateField(auto_now_add=True, null=True)

    def get_absolute_url(self):
        return reverse('film', kwargs={'pk': self.film_id})

    def __str__(self):
        return self.comment_author





class New(models.Model):
    """
    Модель новостей.
    Имеются поля: title - название новости,
    description - Текст новости
    """
    title = models.CharField(max_length=50, verbose_name='Заголовок')
    description = models.TextField(verbose_name='Текст')

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('adminka')

class Poster(models.Model):
    """
    Модель Слайдера. Данная модель будет работать только при 3 слайдах и только после создания фильмов!!!
    Имеются поля: image - изображение которое будет на слайде,
    title - Некое описание слайда,
    film - фильм который относится к этому слайду
    """
    image = models.ImageField(verbose_name='слайд 1')
    title = models.CharField(verbose_name='название слайда', max_length=50)
    film = models.ForeignKey(Film, on_delete=models.CASCADE, related_name='film', null=True)

    def __str__(self):
        return self.title