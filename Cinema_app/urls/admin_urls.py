from django.urls import path
from Cinema_app.views import admin_views as views

urlpatterns = [
    path('adminka', views.Adminka.as_view(), name='adminka'),
    path('adminka-update/<int:pk>', views.AdminkaUpdate.as_view(), name='adminka-update'),
    path('adminka-create', views.AdminkaCreate.as_view(), name='adminka-update'),
    path('adminka-delete/<int:pk>', views.AdminkaDelete, name='adminka-delete'),
    path('adminka-delete-page/<int:pk>', views.AdminkaDeletePage.as_view(), name='adminka-delete-page'),

]