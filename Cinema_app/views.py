from django.shortcuts import render, get_object_or_404
from django.views.generic import ListView, DetailView, CreateView, UpdateView
from .models import Film, Comment, Actor, Director
from .forms import UserRegisterForm
from django.http import HttpResponse
from django.urls import reverse_lazy
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.mixins import LoginRequiredMixin
from .forms import CommentForm



# Create your views here.
class RegisterForm(CreateView):
    form_class = UserRegisterForm
    template_name = 'Cinema_app/register.html'
    success_url = reverse_lazy('login')


def show_films(request): #работает класс
    films = Film.objects.all()
    last_active_film = Film.objects.all().order_by('-id')[0]
    last_two_film = Film.objects.all().order_by('-id')[1]
    last_three_film = Film.objects.all().order_by('-id')[2]
    date = {
        'films': films,
        'last_active_film':last_active_film,
        'last_two_film':last_two_film,
        'last_three_film':last_three_film
    }
    return render(request, 'Cinema_app/home.html', context=date)


def film(request, pk):
    some_film = Film.objects.get(pk = pk)
    #form = CommentForm()

    # if request.method == "POST":
    #     form = CommentForm(request.POST)
    #     if form.is_valid():
    #         post = form.save(commit=False)
    # else: , 'form': form
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
    extra_context = {'film_count': 0}
    if Film.objects.filter(poster__isnull=False).count() > 2:
        last_active_film = Film.objects.filter(poster__isnull=False).order_by('-id')[0]
        last_two_film = Film.objects.filter(poster__isnull=False).order_by('-id')[1]
        last_three_film = Film.objects.filter(poster__isnull=False).order_by('-id')[2]
        extra_context['last_active_film'] = last_active_film
        extra_context['last_two_film'] = last_two_film
        extra_context['last_three_film'] = last_three_film
        extra_context['film_count'] = Film.objects.filter(poster__isnull=False).count()




# class FilmDetailView(DetailView):
#     model = Film
#     template_name = "Cinema_app/film.html"




# class FilmFilterView(ListView):
#     model = Film
#     filt = Film.objects.filter(tipe_film='1_type')
#     template_name = "Cinema_app/filter_film.html"
def FilmFilter(request):
    filt = Film.objects.filter(tipe_film='1_type')
    return render(request, "Cinema_app/filter_film.html", {'filt': filt})
def SerialFilter(request):
    filt = Film.objects.filter(tipe_film='2_type')
    return render(request, "Cinema_app/filter_film.html", {'filt': filt})
def MultFilter(request):
    filt = Film.objects.filter(tipe_film='3_type')
    return render(request, "Cinema_app/filter_film.html", {'filt': filt})

def get_grade(request):
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
    film_play = Actor.objects.get(pk=pk).film.all()  #values('title', 'image')
    context = {'actor': actor_name, 'film_play':film_play}
    return render(request, 'Cinema_app/actor.html', context)

def Directorf(request, pk): # f так как нужно различноне название с моделью
    director_name = Director.objects.get(pk=pk)
    film_play = Director.objects.get(pk=pk).film.all()  #values('title', 'image')
    context = {'director': director_name, 'film_play':film_play}
    return render(request, 'Cinema_app/director.html', context)


