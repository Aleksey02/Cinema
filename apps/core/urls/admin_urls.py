from django.urls import path
from apps.core.views import admin_views as views

urlpatterns = [
    path('admin/', views.Adminka.as_view(), name='adminka'),  # adminka??
    # Лучше admin/update/...
    path('admin/update/<int:pk>', views.AdminkaUpdate.as_view(), name='adminka-update'),
    path('admin/create', views.AdminkaCreate.as_view(), name='adminka-update'),
    path('admin/delete/<int:pk>', views.AdminkaDelete, name='adminka-delete'),
    path('admin/delete/page/<int:pk>', views.AdminkaDeletePage.as_view(), name='adminka-delete-page'),

]
