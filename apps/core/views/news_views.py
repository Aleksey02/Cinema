from django.views.generic import ListView, DetailView, CreateView, UpdateView
from apps.core.models import New
from django.shortcuts import redirect
from django.urls import reverse_lazy



class NewsList(ListView):
    model = New
    template_name = 'Cinema_app/news.html'

class NewsDetail(DetailView):
    model = New
    template_name = 'Cinema_app/news-detail.html'

class NewsUpdate(UpdateView):
    model = New
    template_name = 'Cinema_app/adminka-update.html'
    fields = '__all__'

def NewsDelete(request, pk):
    news = New.objects.get(pk=pk)
    news.delete()
    return redirect('adminka')

class NewsDeletePage(DetailView):
    model = New
    template_name = 'Cinema_app/news-delete.html'

class NewsCreate(CreateView):
    model = New
    template_name = 'Cinema_app/adminka-update.html'
    fields = '__all__'
    success_url = reverse_lazy('adminka')