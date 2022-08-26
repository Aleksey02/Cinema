from django.shortcuts import render
from docutils.nodes import field_name
from rest_framework import viewsets
# from apps.api.models import Checkbox
# from apps.api.serializers import CheckboxSerializer
from apps.core.models import Film, Actor
from apps.api.serializers import CinemaSerializer
from django_filters.rest_framework import DjangoFilterBackend
from django_filters import rest_framework as filters
import django_filters

# Create your views here.

# class CheckboxViewSet(viewsets.ModelViewSet):
#     queryset = Checkbox.objects.all()
#     serializer_class = CheckboxSerializer
class CharFilterInFilter(filters.BaseInFilter, filters.CharFilter):
    pass

class FilmFilter(django_filters.FilterSet):
    actor = filters.CharFilter(field_name='actor__full_name')
    director = filters.CharFilter(field_name='director__full_name')
    ganre = filters.MultipleChoiceFilter(field_name='ganre',choices=Film.CHOICES)

    class Meta:
        model = Film
        fields = ['ganre', 'year','actor', 'id', 'director', 'title', 'country', 'tipe_film']


class CinemaViewSet(viewsets.ModelViewSet):
    queryset = Film.objects.prefetch_related('actor','director').all()
    serializer_class = CinemaSerializer
    filter_backends = (DjangoFilterBackend,)
    filterset_class = FilmFilter



# class FooFilter(BaseFilterSet):
#     foo = django_filters.filters.ModelMultipleChoiceFilter(
#         field_name='attr__uuid',
#         to_field_name='uuid',
#         queryset=Foo.objects.all(),
#     )