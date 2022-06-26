from django.shortcuts import render, get_object_or_404, redirect
from django.views.generic import ListView, DetailView, CreateView, UpdateView
from apps.core.models import Film, Comment, Actor, Director, New, Poster
from apps.core.forms import UserRegisterForm
from django.http import HttpResponse
from django.urls import reverse_lazy
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.mixins import LoginRequiredMixin
from apps.core.forms import CommentForm
from django.contrib.auth.models import User


# Create your views here.
class RegisterForm(CreateView):
    form_class = UserRegisterForm
    template_name = 'Cinema_app/register.html'
    success_url = reverse_lazy('login')


def film(request, pk):
    some_film = Film.objects.get(pk=pk)
    date = {'film': some_film}
    return render(request, 'Cinema_app/film.html', context=date)


class AddCommentView(LoginRequiredMixin, CreateView):
    model = Comment
    template_name = 'Cinema_app/add_comment.html'
    form_class = CommentForm

    def form_valid(self, form):
        form.instance.film_id = self.kwargs['pk']
        return super().form_valid(form)


class FilmView(ListView):
    model = Film
    template_name = "Cinema_app/home.html"

    """python manage.py makemigrations core"""
    """python manage.py migrate"""
    """Далее ниже уберешь комменты"""

    # posters = Poster.objects.all()
    # extra_context = {'film_count': posters.count(), 'posters': posters}
    # if posters.count() >= 3:
    #     extra_context['slide1'] = Poster.objects.all()[posters.count() - 3]
    #     extra_context['slide2'] = Poster.objects.all()[posters.count() - 2]
    #     extra_context['slide3'] = Poster.objects.all()[posters.count() - 1]


def FilmFilter(request, type_film):
    filt = Film.objects.filter(tipe_film=type_film)
    return render(request, "Cinema_app/filter_film.html", {'filt': filt})


def get_grade(request):  # Не работает
    if request.method == 'POST':
        form = GradeForm(request.POST)
    else:
        form = GradeForm()
    return render(request, 'film.html', {'form': form})


class ActorView(DetailView):
    model = Actor
    template_name = 'Cinema_app/actor.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['film_con'] = Film.objects.get(pk=pk).actor_set.all()
        return context


def Actorf(request, pk):
    actor_name = Actor.objects.get(pk=pk)
    film_play = Actor.objects.get(pk=pk).actor.all()  # values('title', 'image')
    context = {'actor': actor_name, 'film_play': film_play}
    return render(request, 'Cinema_app/actor.html', context)


def Directorf(request, pk):  # f так как нужно различноне название с моделью
    director_name = Director.objects.get(pk=pk)
    film_play = Director.objects.get(pk=pk).director.all()  # values('title', 'image')
    context = {'director': director_name, 'film_play': film_play}
    return render(request, 'Cinema_app/director.html', context)


def GanreFilter(request, ganre):
    filt = Film.objects.filter(ganre)
    success_url = reverse_lazy('film')
    return render(request, "Cinema_app/filter_film.html", {'filt': filt})


class UserInfo(ListView):
    model = User
    template_name = 'Cinema_app/user-page.html'
