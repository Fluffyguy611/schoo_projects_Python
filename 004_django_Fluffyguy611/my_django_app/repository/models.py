from django.db import models
from django.core.exceptions import ValidationError
from django.utils.translation import gettext_lazy as _
from django.urls import reverse
from django.contrib.auth.models import User
from django.db.models import UniqueConstraint


class Category(models.Model):
    categories_choice = [
        ('Books', 'Books'),
        ('Movies', 'Movies'),
        ('Cds', 'CDs'),
    ]
    name = models.CharField(max_length=255, db_index=True)
    slug = models.SlugField(max_length=255, choices=categories_choice, unique=True)

    class Meta:
        verbose_name_plural = 'categories'
#    def get_absolute_url(self):
#        return reverse('repository:category_index', args=[self.slug])

    def __str__(self):
        return self.name


def validate_ISBN(value):
    if len(value) != 13:
        raise ValidationError('Value is not an ISBN number')
    else:
        return value


class Book(models.Model):
    Book_Genre = [
        ('Thriller', 'Thriller'),
        ('Drama', 'Drama'),
        ('Horror', 'Horror'),
        ('Action', 'Action'),
        ('Sci-fi', 'Sci-fi'),
        ('Historical', 'Historical'),
        ('Documentary', 'Documentary'),
        ('None', 'None'),
    ]

    category = models.ForeignKey(Category, related_name='Books', on_delete=models.CASCADE)
    title = models.CharField(max_length=255)
    author = models.CharField(max_length=255, blank=True)
    description = models.TextField(blank=True)
    slug = models.SlugField(max_length=255, unique=True)
    genre = models.CharField(max_length=11, choices=Book_Genre)
    ISBN = models.CharField(max_length=13, unique=True, validators=[validate_ISBN])
    is_active = models.BooleanField(default=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    can_be_deposited_by = models.ManyToManyField(User, through='Rent', blank=True, name='deposit')

    class Meta:
        verbose_name_plural = 'Books'
        ordering = ('-created',)
        constraints = [
            models.UniqueConstraint(fields=['title', 'author', 'genre'], name='unique_book')
        ]

    def get_absolute_url(self):
        return reverse('repository:single_book', args=[self.slug])

    def __str__(self):
        return self.title


class Movie(models.Model):
    Movie_Genre = [
        ('Thriller', 'Thriller'),
        ('Drama', 'Drama'),
        ('Horror', 'Horror'),
        ('Action', 'Action'),
        ('Sci-fi', 'Sci-fi'),
        ('Historical', 'Historical'),
        ('Documentary', 'Documentary'),
        ('None', 'None'),
    ]

    category = models.ForeignKey(Category, related_name='Movies', on_delete=models.CASCADE)
    title = models.CharField(max_length=255)
    director = models.CharField(max_length=255, default='None')
    description = models.TextField(blank=True)
    slug = models.SlugField(max_length=255, unique=True)
    genre_1 = models.CharField(max_length=11, choices=Movie_Genre, blank=True)
    genre_2 = models.CharField(max_length=11, choices=Movie_Genre, blank=True)
    genre_3 = models.CharField(max_length=11, choices=Movie_Genre, blank=True)
    duration = models.IntegerField(blank=True)
    is_active = models.BooleanField(default=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    can_be_deposited_by = models.ManyToManyField(User, through='Rent', blank=True)

    class Meta:
        verbose_name_plural = 'Movies'
        ordering = ('-created',)
        constraints = [
            models.UniqueConstraint(fields=['title', 'director', 'duration'], name='unique_movie')
        ]

    def get_absolute_url(self):
        return reverse('repository:single_movie', args=[self.slug])

    def __str__(self):
        return self.title


class CD(models.Model):
    CD_Genre = [
        ('Rap', 'Rap'),
        ('Pop', 'Pop'),
        ('Classic', 'Classic'),
        ('Rock', 'Rock'),
        ('Metal', 'Metal'),
        ('Heavy metal', 'Heavy metal'),
        ('Disco-polo', 'Disco-polo'),
        ('None', 'None'),
    ]

    category = models.ForeignKey(Category, related_name='CDs', on_delete=models.CASCADE)
    title = models.CharField(max_length=255)
    band = models.CharField(max_length=255, blank=True)
    music_list = models.TextField(blank=True)
    slug = models.SlugField(max_length=255, unique=True)
    genre_1 = models.CharField(max_length=11, choices=CD_Genre, blank=True)
    genre_2 = models.CharField(max_length=11, choices=CD_Genre, blank=True)
    is_active = models.BooleanField(default=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    can_be_deposited_by = models.ManyToManyField(User, through='Rent', blank=True, related_name='deposit')

    class Meta:
        verbose_name_plural = 'CDs'
        ordering = ('-created',)
        constraints = [
            models.UniqueConstraint(fields=['genre_1', 'genre_2', 'music_list'], name='unique_cd')
        ]

    def get_absolute_url(self):
        return reverse('repository:single_cd', args=[self.slug])

    def __str__(self):
        return self.title


class Rent(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    depositet_book = models.OneToOneField(Book, null=True, blank=True, on_delete=models.CASCADE)
    depositet_movie = models.OneToOneField(Movie, null=True, blank=True, on_delete=models.CASCADE)
    depositet_cd = models.OneToOneField(CD, null=True, blank=True, on_delete=models.CASCADE)
    deposit_date = models.DateField()
    deposit_length = models.DateField()
