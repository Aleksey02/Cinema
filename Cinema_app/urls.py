from django.contrib import admin
from django.urls import path
from . import views
from django.contrib.auth import views as auth_view


urlpatterns = [
    path('', views.FilmView.as_view(), name='home'),
    path('register/', views.RegisterForm.as_view(), name='register'),
    path('login/', auth_view.LoginView.as_view(template_name='Cinema_app/login.html'), name='login'),
    path('logout/', auth_view.LogoutView.as_view(template_name='Cinema_app/logout.html'), name='logout'),
    path('film/<int:pk>/comment/', views.AddCommentView.as_view(),name='comment'),
    path('film/<int:pk>', views.film, name='film'),
    path('film/filter_film', views.FilmFilter, name= 'filter_film'),
    path('film/filter_serial', views.SerialFilter, name= 'filter_serial'),
    path('film/filter_mult', views.MultFilter, name= 'filter_mult'),
    path('actor/<int:pk>/', views.Actorf, name='actor'),
    path('director/<int:pk>/', views.Directorf, name='director'),
    path('adminka', views.Adminka.as_view(), name='adminka'),
    path('adminka-update/<int:pk>', views.AdminkaUpdate.as_view(), name='adminka-update'),
    path('adminka-create', views.AdminkaCreate.as_view(), name='adminka-update'),
    path('adminka-delete/<int:pk>', views.AdminkaDelete, name='adminka-delete'),
    path('adminka-delete-page/<int:pk>', views.AdminkaDeletePage.as_view(), name='adminka-delete-page'),
    path('news', views.NewsList.as_view(), name='news'),
    path('news-detail/<int:pk>', views.NewsDetail.as_view(), name='news-detail'),
    path('news-update/<int:pk>', views.NewsUpdate.as_view(), name='news-update'),
    path('news-delete/<int:pk>', views.NewsDelete, name='news-delete'),
    path('news-delete-page/<int:pk>', views.NewsDeletePage.as_view(), name='news-delete-page'),
    path('news-create', views.NewsCreate.as_view(), name='news-create'),

]