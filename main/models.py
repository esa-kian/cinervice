from django.db import models
from django import forms
# from django.contrib.gis.geoip2 import GeoIP2
# Create your models here.

class People(models.Model):
    image = models.ImageField(upload_to='static/images/people',null=True)
    full_name = models.CharField(max_length=300)
    birth_date = models.DateTimeField()
    birth_place = models.CharField(max_length=300,null=True)
    comment = models.TextField(null=True)
    point = models.FloatField(default=0)
    count = models.IntegerField(default=0)

    def __str__(self):
        return self.full_name


class Movie(models.Model):
    image = models.ImageField(upload_to='static/images/movies',null=True)
    title = models.CharField(max_length=200)
    publish_year = models.DateTimeField()
    comment = models.TextField(null=True)
    genre = models.CharField(max_length=100)
    point = models.FloatField(default=0)
    count = models.IntegerField(default=0)

    def __str__(self):
        return self.title

class Series(models.Model):
    image = models.ImageField(upload_to='static/images/series',null=True)
    title = models.CharField(max_length=200)
    start_year = models.DateTimeField()
    end_year = models.DateTimeField()
    comment = models.TextField(null=True)
    genre = models.CharField(max_length=100)
    point = models.FloatField(default=0)
    count = models.IntegerField(default=0)

    def __str__(self):
        return self.title

class Role(models.Model):
    TYPE_OF_PRODUCT = [
        ('M', 'Movie'),
        ('S', 'Serial'),
    ]
    TYPE_OF_ROLE = [
        ('A', 'Actor'),
        ('D', 'Director'),
        ('W', 'Writer'),
    ]
    person = models.ForeignKey(People, on_delete = models.CASCADE)
    movie = models.ForeignKey(Movie, on_delete = models.CASCADE, null = True, blank = True)
    serial = models.ForeignKey(Series, on_delete = models.CASCADE, null = True, blank = True)
    type_of_product = forms.MultipleChoiceField(
        required=False,
        widget=forms.CheckboxSelectMultiple,
        choices=TYPE_OF_PRODUCT,
    )
    type_of_role = forms.MultipleChoiceField(
        required=False,
        widget=forms.CheckboxSelectMultiple,
        choices=TYPE_OF_ROLE,
    )
    
    def __str__(self):
        if(self.movie is None):
            return self.person.full_name + ': [Serial]: ' + self.serial.title
        elif (self.serial is None):
            return self.person.full_name + ': [Movie]: ' + self.movie.title

class Cinema(models.Model):
    image = models.ImageField(upload_to='static/images/cinemas', null=True, blank=True)
    name = models.CharField(max_length=300)
    establish_date = models.DateTimeField()
    address = models.TextField(null = True)
    point = models.FloatField(default=0)
    count = models.IntegerField(default=0)
    movie = models.ManyToManyField(Movie)

    def __str__(self):
        return self.name

class Contact_Form(models.Model):
    first_name = models.CharField(max_length=300)
    last_name = models.CharField(max_length=300)
    country = models.CharField(max_length=300)
    subject = models.TextField(null=False, blank=False)
    def __str__(self):
        return self.first_name + ' ' + self.last_name + ': ' + self.subject