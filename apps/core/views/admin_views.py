from django.views.generic import ListView, DetailView, CreateView, UpdateView
from apps.core.models import Film, New, Poster
from django.urls import reverse_lazy
from django.shortcuts import redirect


class Adminka(ListView):
    model = Film
    template_name = 'Cinema_app/adminka.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['news'] = New.objects.all()
        context['posters'] = Poster.objects.all().order_by()
        context['postersCount'] = Poster.objects.all().count()
        return context


class AdminkaUpdate(UpdateView):
    model = Film
    template_name = 'Cinema_app/adminka-update.html'
    fields = '__all__'

    def get_absolute_url(self):
        return reverse('adminka')


class AdminkaDeletePage(DetailView):
    model = Film
    template_name = 'Cinema_app/adminka-delete.html'


def AdminkaDelete(request, pk):
    film = Film.objects.get(pk=pk)
    film.delete()
    return redirect('adminka')


class AdminkaCreate(CreateView):
    model = Film
    template_name = 'Cinema_app/adminka-update.html'
    fields = '__all__'
    success_url = reverse_lazy('adminka')
