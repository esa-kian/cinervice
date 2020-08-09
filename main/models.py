from django.db import models
from django import forms
from django.contrib import auth
from django.conf import settings


class People(models.Model):
    image = models.ImageField(upload_to='static/images/people',null=True)
    full_name = models.CharField(max_length=300)
    birth_date = models.DateTimeField(null = True)
    birth_place = models.CharField(max_length=300,null=True)
    comment = models.TextField(null=True)

    def __str__(self):
        return self.full_name

class Movie(models.Model):
    image = models.ImageField(upload_to='static/images/movies',null=True)
    title = models.CharField(max_length=200)
    publish_year = models.DateTimeField(null = True)
    comment = models.TextField(null=True)
    genre = models.CharField(max_length=100)

    def __str__(self):
        return self.title

class Series(models.Model):
    image = models.ImageField(upload_to='static/images/series',null=True)
    title = models.CharField(max_length=200)
    start_year = models.DateTimeField(null = True)
    end_year = models.DateTimeField(null = True)
    comment = models.TextField(null=True)
    genre = models.CharField(max_length=100)

    def __str__(self):
        return self.title

class Cinema(models.Model):
    image = models.ImageField(upload_to='static/images/cinemas', null=True, blank=True)
    name = models.CharField(max_length=300)
    establish_date = models.DateTimeField(null = True)
    address = models.TextField(null = True)
    latitude = models.IntegerField(null=True, blank = True)
    longitude = models.IntegerField(null=True, blank = True)
    movie = models.ManyToManyField(Movie)

    def __str__(self):
        return self.name


class Movies_Vote(models.Model):
    movie = models.ForeignKey(Movie, null=False, on_delete = models.CASCADE)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, null=False, on_delete=models.CASCADE)
    vote = models.IntegerField(null=False)


class Series_Vote(models.Model):
    serial = models.ForeignKey(Series, null=False, on_delete = models.CASCADE)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, null=False, on_delete=models.CASCADE)
    vote = models.IntegerField(null=False)

class People_Vote(models.Model):
    people = models.ForeignKey(People, null=False, on_delete = models.CASCADE)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, null=False, on_delete=models.CASCADE)
    vote = models.IntegerField(null=False)

class Cinema_Vote(models.Model):
    cinema = models.ForeignKey(Cinema, null=False, on_delete = models.CASCADE)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, null=False, on_delete=models.CASCADE)
    vote = models.IntegerField(null=False)

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
    type_of_product = models.CharField(max_length=1, null = True, choices=TYPE_OF_PRODUCT)
    type_of_role = models.CharField(max_length=1, null = True, choices=TYPE_OF_ROLE)
    
    def __str__(self):
        if(self.movie is None):
            return self.person.full_name + ': [Serial]: ' + self.serial.title
        elif (self.serial is None):
            return self.person.full_name + ': [Movie]: ' + self.movie.title


class Contact_Form(models.Model):
    email = models.EmailField(max_length=300, null=False)
    subject = models.TextField(null=False, blank=False)
    def __str__(self):
        return self.email + ' ' + ': ' + self.subject