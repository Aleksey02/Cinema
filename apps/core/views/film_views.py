from django.shortcuts import render, get_object_or_404, redirect
from django.views.generic import ListView, DetailView, CreateView, UpdateView
from apps.core.models import Film, Comment, Actor, Director, New, Poster
from apps.core.forms import UserRegisterForm, SearchForm
from django.http import HttpResponse
from django.urls import reverse_lazy
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.mixins import LoginRequiredMixin
from apps.core.forms import CommentForm
from django.contrib.auth.models import User
import requests



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
    paginate_by = 30
    ordering = ['-year']

    """python manage.py makemigrations core"""
    """python manage.py migrate"""
    """Далее ниже уберешь комменты"""


    # posters = Poster.objects.all()
    # extra_context = {'film_count': posters.count(), 'posters': posters}
    # if posters.count() >= 3:
    #     extra_context['slide1'] = Poster.objects.all()[posters.count() - 3]
    #     extra_context['slide2'] = Poster.objects.all()[posters.count() - 2]
    #     extra_context['slide3'] = Poster.objects.all()[posters.count() - 1]





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
    film_play = Film.objects.filter(actor=pk)  # values('title', 'image')
    context = {'actor': actor_name, 'film_play': film_play}
    return render(request, 'Cinema_app/actor.html', context)


def Directorf(request, pk):  # f так как нужно различноне название с моделью
    director_name = Director.objects.get(pk=pk)
    film_play = Director.objects.get(pk=pk).director.all()  # values('title', 'image')
    context = {'director': director_name, 'film_play': film_play}
    return render(request, 'Cinema_app/director.html', context)


def FilmFilter(request, value, filter):
    if filter=='ganre':
        filt = Film.objects.filter(ganre__contains=value).order_by('-year')
    elif filter=='country':
        filt = Film.objects.filter(country__contains=value).order_by('-year')
    elif filter=='search':
        filt = Film.objects.filter(title__icontains=request.GET.get('film'))
        value=request.GET.get('film')
    elif filter=='year':
        filt = Film.objects.filter(year=value).order_by('-year')
    elif filter=='age':
        filt = Film.objects.filter(lim_age=value).order_by('-year')
        value+='+'
    else:
        filt = Film.objects.filter(tipe_film=value).order_by('-year')
        value=0
    return render(request, "Cinema_app/filter_film.html", {'filt': filt, 'value':value})

# def FilmFilter(request, type_film):
#     filt = Film.objects.filter(tipe_film=type_film).order_by('-year')
#     return render(request, "Cinema_app/filter_film.html", {'filt': filt})

# def CountryFilter(request, country):
#     filt = Film.objects.filter(country__contains=country).order_by('-year')
#     return render(request, "Cinema_app/filter_film.html", {'filt': filt})


class UserInfo(ListView):
    model = User
    template_name = 'Cinema_app/user-page.html'


def my_api(request):
    movie = id()
    for i in movie:
        response = requests.get(f'https://api.kinopoisk.dev/movie?field=id&search={i}&token=KBVX3GZ-DPY41PN-M7WF0DG-PE0RCJH')
        if response.text == '{"message":"id not found"}':
            continue
        res=response.json()
        name = res['name']
        desc = res['description']
        ganre = [g['name'] for g in  res['genres']]
        tipe_film = res['type']
        year = res['year']
        image = res["poster"]['url']
        lim_age = res['ageRating']
        if lim_age==0 and ('мультфильм' not in ganre) and ('детский' not in ganre):
            continue
        country = [c['name'] for c in  res['countries']]



        actor = [a['name'] for a in res['persons'] if a['enProfession']=='actor']
        newActor=[]

        director = [d['name'] for d in res['persons'] if d['enProfession']=='producer']
        newDirector=[]
        if name==None or desc==None or year==None or lim_age==None or country==None:
            continue
        country = country[0]
        newFilm = Film.objects.create(
            title=name,
            description=desc,
            ganre=ganre,
            tipe_film=tipe_film,
            year=year,
            image=image,
            lim_age=lim_age,
            country=country,

        )
        newFilm.save()
        for act in actor:
            if act=='' or act==None:
                continue
            newActor=(Actor.objects.create(full_name=act))
            newFilm.actor.add(newActor.id)
        for dir in director:
            if dir=='' or dir==None:
                continue
            newDirector=(Director.objects.create(full_name=dir))
            newFilm.director.add(newDirector.id)
    return HttpResponse('movie dowload is finished')

def id():
    response = requests.get(
        'https://api.kinopoisk.dev/movie?token=KBVX3GZ-DPY41PN-M7WF0DG-PE0RCJH&limit=2000')
    res = response.json()
    lst = [i['id'] for i in res['docs']]
    return lst


def Profile(request):

    return render(request, 'registration/profile.html')