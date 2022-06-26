from django.views.generic import ListView, DetailView, CreateView, UpdateView
from apps.core.models import Poster
from django.urls import reverse_lazy
from django.shortcuts import redirect


class PosterCreate(CreateView):
    model = Poster
    template_name = 'Cinema_app/adminka-update.html'
    fields = '__all__'
    success_url = reverse_lazy('adminka')


class PosterUpdate(UpdateView):
    model = Poster
    template_name = 'Cinema_app/adminka-update.html'
    fields = '__all__'


class PosterDeletePage(DetailView):
    model = Poster
    template_name = 'Cinema_app/news-delete.html'


def PosterDelete(request, pk):
    poster = Poster.objects.get(pk=pk)
    poster.delete()
    return redirect('adminka')
