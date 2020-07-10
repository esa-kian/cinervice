from django.contrib import admin
from .models import Movie, Series, People, Cinema, Role, Contact_Form

# Register your models here.
admin.site.register(Movie)
admin.site.register(Series)
admin.site.register(People)
admin.site.register(Cinema)
admin.site.register(Role)
admin.site.register(Contact_Form)