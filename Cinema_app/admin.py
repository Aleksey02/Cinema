from django.contrib import admin
from .models import Film, Comment, Actor, Director, New
# Register your models here.
admin.site.register(Film)
admin.site.register(Comment)
admin.site.register(Actor)
admin.site.register(Director)
admin.site.register(New)