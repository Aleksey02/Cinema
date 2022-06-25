from django.urls import path
from Cinema_app.views import poster_views as views


urlpatterns = [
    path('poster-create', views.PosterCreate.as_view(), name='poster-create'),
    path('poster-update/<int:pk>', views.PosterUpdate.as_view(), name='poster-update'),
    path('poster-delete-page/<int:pk>', views.PosterDeletePage.as_view(), name='poster-delete-page'),
    path('poster-delete/<int:pk>', views.PosterDelete, name='poster-delete'),

]