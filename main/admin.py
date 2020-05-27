from django.contrib import admin
from .models import Movie, Series, People, Cinema

# Register your models here.
admin.site.register(Movie)
admin.site.register(Series)
admin.site.register(People)
admin.site.register(Cinema)