from django.contrib import admin
from django.urls import path
from Cinema_app.views import film_views as views
from django.contrib.auth import views as auth_view


urlpatterns = [
    path('', views.FilmView.as_view(), name='home'),
    path('film/<int:pk>/comment/', views.AddCommentView.as_view(), name='comment'),
    path('film/<int:pk>', views.film, name='film'),
    path('film/<str:type_film>', views.FilmFilter, name='filter_film'),
    path('film/filter_ganre/<str:ganre>', views.GanreFilter, name='filter_ganre'),

    path('register/', views.RegisterForm.as_view(), name='register'),
    path('login/', auth_view.LoginView.as_view(template_name='Cinema_app/login.html'), name='login'),
    path('logout/', auth_view.LogoutView.as_view(template_name='Cinema_app/logout.html'), name='logout'),



    path('actor/<int:pk>/', views.Actorf, name='actor'),
    path('director/<int:pk>/', views.Directorf, name='director'),








]