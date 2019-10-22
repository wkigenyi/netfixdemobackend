from django.contrib import admin
from .models import Rating,Movie,Awards,Actor,Director,Writer,Genre
# Register your models here.
admin.site.register(Rating)
admin.site.register(Movie)
admin.site.register(Awards)
admin.site.register(Actor)
admin.site.register(Director)
admin.site.register(Writer)
admin.site.register(Genre)