from django.urls import path, include
from apps.core.views import film_views as views
from django.contrib.auth import views as auth_view

urlpatterns = [
    path('', views.FilmView.as_view(), name='home'),
    path('film/<int:pk>/comment/', views.AddCommentView.as_view(), name='comment'),
    path('film/<int:pk>', views.film, name='film'),
    path('film/filter/<str:filter>/<str:value>', views.FilmFilter, name='filter_film'),

    path('register/', views.RegisterForm.as_view(), name='register'),
    path('login/', auth_view.LoginView.as_view(template_name='Cinema_app/login.html'), name='login'),
    #path('logout/', auth_view.LogoutView.as_view(template_name='registration/logout.html'), name='mylogout'),
    path('profile/', views.Profile, name='profile'),

    path('actor/<int:pk>/', views.Actorf, name='actor'),
    path('director/<int:pk>/', views.Directorf, name='director'),

    path('user-page/', views.UserInfo.as_view(), name='userPage'),
    path('api/', views.my_api, name='my_api'),
]

urlpatterns += [
    path("login/", auth_view.LoginView.as_view(), name="login"),
    path("logout/", auth_view.LogoutView.as_view(template_name='registration/logout.html'), name="logout"),
    path(
        "password_change/", auth_view.PasswordChangeView.as_view(), name="password_change"
    ),
    path(
        "password_change/done/",
        auth_view.PasswordChangeDoneView.as_view(),
        name="password_change_done",
    ),
    path("password_reset/", auth_view.PasswordResetView.as_view(), name="password_reset"),
    path(
        "password_reset/done/",
        auth_view.PasswordResetDoneView.as_view(),
        name="password_reset_done",
    ),
    path(
        "reset/<uidb64>/<token>/",
        auth_view.PasswordResetConfirmView.as_view(),
        name="password_reset_confirm",
    ),
    path(
        "reset/done/",
        auth_view.PasswordResetCompleteView.as_view(),
        name="password_reset_complete",
    ),
]