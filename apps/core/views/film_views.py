from django.shortcuts import render, get_object_or_404, redirect
from django.views.generic import ListView, DetailView, CreateView, UpdateView
from apps.core.models import Film, Comment, Actor, Director, New, Poster
from apps.core.forms import UserRegisterForm, SearchForm, LoginUserForm, CommentForm
from django.http import HttpResponse
from django.urls import reverse_lazy
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.models import User
import requests
import random
from django.contrib.auth import views as auth_views
from django.core.paginator import Paginator



# Create your views here.
class RegisterForm(CreateView):
    form_class = UserRegisterForm
    template_name = 'Cinema_app/register.html'
    success_url = reverse_lazy('login')
    extra_context = {'title': 'Registraion'}

def film(request, pk):
    some_film = Film.objects.prefetch_related('actor', 'director').get(pk=pk)
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

    def get_queryset(self):
        return Film.objects.order_by('-year').values('title', 'image', 'pk')
    """python manage.py makemigrations core"""
    """python manage.py migrate"""
    """Далее ниже уберешь комменты"""

    posters = Poster.objects.all()
    extra_context = {'film_count': posters.count(), 'posters': posters}
    if posters.count() >= 3:
        extra_context['slide1'] = Poster.objects.all()[posters.count() - 3]
        extra_context['slide2'] = Poster.objects.all()[posters.count() - 2]
        extra_context['slide3'] = Poster.objects.all()[posters.count() - 1]





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




def FilmFilter(request, value, filter):
    match filter:
        case 'ganre':
            filt = Film.objects.filter(ganre__contains=value).order_by('-year').values('title', 'image', 'pk')
        case 'country':
            filt = Film.objects.filter(country__contains=value).order_by('-year').values('title', 'image', 'pk')
        case 'search':
            value=request.GET.get('film')
            filt = Film.objects.filter(title__icontains=value).values('title', 'image', 'pk')
        case 'year':
            filt = Film.objects.filter(year=value).order_by('-year').values('title', 'image', 'pk')
        case 'age':
            filt = Film.objects.filter(lim_age=value).order_by('-year').values('title', 'image', 'pk')
            value+='+'
        case 'actor':
            value = Actor.objects.get(pk=value)
            filt = Film.objects.filter(actor=value).values('title', 'image', 'pk')
        case 'director':
            value = Director.objects.get(pk=value)
            filt = Film.objects.filter(director=value).values('title', 'image', 'pk')
        case _:
            filt = Film.objects.filter(tipe_film=value).order_by('-year').values('title', 'image', 'pk')
            value=0
    paginator = Paginator(filt, 5)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    return render(request, "Cinema_app/filter_film.html", {'page_obj': page_obj, 'filt': filt, 'value':value})

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
        print('asd')
        response = requests.get(f'https://api.kinopoisk.dev/movie?field=id&search={i}&token=KBVX3GZ-DPY41PN-M7WF0DG-PE0RCJH')
        if response.text == '{"message":"id not found"}':
            continue
        try:

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
            if name==None or desc==None or year==None or lim_age==None or country==None or country=='':
                continue
            country = list(country)
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

            for act in actor:
                if act=='' or act==None:
                    continue
                try:
                    hasActor = Actor.objects.get(full_name=act)
                    newFilm.actor.add(hasActor.id)
                except:
                    newActor=(Actor.objects.create(full_name=act))
                    newFilm.actor.add(newActor.id)
                    newActor.save()
            for dir in director:
                if dir=='' or dir==None:
                    continue
                try:
                    hasDirector = Director.objects.get(full_name=dir)
                    newFilm.director.add(hasDirector.id)
                except:
                    newDirector = (Director.objects.create(full_name=dir))
                    newFilm.director.add(newDirector.id)
                newDirector.save()
            all_comments=[
                [{
                    'author_name': 'Алексей',
                    'text': 'Фильм класный',
                }],[{
                    'author_name': 'Анна',
                    'text': 'Фильм супер',
                },{
                    'author_name': 'Максим',
                    'text': 'Фильм отстой',
                }],[
                    {
                        'author_name': 'Михаил',
                        'text': 'кайф',
                    }, {
                        'author_name': 'Саня',
                        'text': 'обязательно пересмотрю',
                    }, {
                        'author_name': 'Лиза',
                        'text': 'Смотрела и лучше',
                    },{
                        'author_name': 'Дед Мазай',
                        'text': 'Мало зайцев',
                    }
                ]
            ]

            choiceComment = random.choice(all_comments)
            for commentInfo  in choiceComment:
                comment = Comment.objects.create(
                    comment_author = commentInfo['author_name'],
                    comment_text = commentInfo['text'],
                    film = newFilm
                )
                comment.save()
            newFilm.save()
            print(newFilm.title)
        except:
            continue
    return HttpResponse('movie dowload is finished')

def id():
    response = requests.get(
        'https://api.kinopoisk.dev/movie?token=KBVX3GZ-DPY41PN-M7WF0DG-PE0RCJH&limit=40100')
    res = response.json()
    lst = [i['id'] for i in res['docs']]
    return lst


def Profile(request):
    return render(request, 'registration/profile.html')


def password_reset_request(request):
	if request.method == "POST":
		password_reset_form = PasswordResetForm(request.POST)
		if password_reset_form.is_valid():
			data = password_reset_form.cleaned_data['email']
			associated_users = User.objects.filter(Q(email=data))
			if associated_users.exists():
				for user in associated_users:
					subject = "Password Reset Requested"
					email_template_name = "registration/password_reset_email.txt"
					c = {
					"email":user.email,
					'domain':'127.0.0.1:8000',
					'site_name': 'Cinema',
                        "uid": urlsafe_base64_encode(force_bytes(user.pk)).decode(),
                        "user": user,
					'token': default_token_generator.make_token(user),
					'protocol': 'http',
					}
					email = render_to_string(email_template_name, c)
					try:
						send_mail(subject, email, 'lyosha2002stich@gmail.com' , [user.email], fail_silently=False)
					except BadHeaderError:
						return HttpResponse('Invalid header found.')
					return redirect ("/password_reset/done/")
	password_reset_form = PasswordResetForm()
	return render(request=request, template_name="registration/password_reset.html", context={"password_reset_form":password_reset_form})

class LoginUser(auth_views.LoginView):
    form_class = LoginUserForm
    extra_context = {'title': 'Login'}
    def get_success_url(self):
        return reverse_lazy('home')