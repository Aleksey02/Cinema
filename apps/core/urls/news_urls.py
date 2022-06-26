from django.urls import path
from apps.core.views import news_views as views

urlpatterns = [
    path('news', views.NewsList.as_view(), name='news'),
    path('news-detail/<int:pk>', views.NewsDetail.as_view(), name='news-detail'),
    path('news-update/<int:pk>', views.NewsUpdate.as_view(), name='news-update'),
    path('news-delete/<int:pk>', views.NewsDelete, name='news-delete'),
    path('news-delete-page/<int:pk>', views.NewsDeletePage.as_view(), name='news-delete-page'),
    path('news-create', views.NewsCreate.as_view(), name='news-create'),
]
