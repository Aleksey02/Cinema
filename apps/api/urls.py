from django.urls import path, include
from rest_framework import routers
#from apps.api.views import CheckboxViewSet
from apps.api.views import CinemaViewSet

router = routers.DefaultRouter()
#router.register('checkbox', CheckboxViewSet)
router.register('cinema', CinemaViewSet)

urlpatterns = [
    path('', include(router.urls)),
]