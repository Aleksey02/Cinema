from rest_framework import serializers
#from apps.api.models import Checkbox
from apps.core.models import Film, Actor, Director
from django_filters import rest_framework as filters

# class CheckboxSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Checkbox
#         fields = '__all__'

# class CinemaSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Film
#         fields = '__all__'
#
# class ActorSerializer(serializers.ModelSerializer):
#     actors = CinemaSerializer(source='actor', many=True)
#     class Meta:
#         model = Actor
#         fields = ('actors',)

class CinemaSerializer(serializers.ModelSerializer):
    actor = serializers.SlugRelatedField(many=True, read_only=True, slug_field='full_name')
    director = serializers.SlugRelatedField(many=True, read_only=True, slug_field='full_name')


    class Meta:
        model = Film
        fields = ('__all__')


class CinemaListSerializer(serializers.ModelSerializer):
    actors = CinemaSerializer(source='actor', many=True, read_only=True)
    directors = CinemaSerializer(source='director', many=True, read_only=True)
    class Meta:
        model = Actor, Director
        fields = ('__all__')

