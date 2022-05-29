from django.contrib import admin

from .models import Category, Book, Movie, CD, Rent


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['name', 'slug']


@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    list_display = ['title', 'author', 'slug', 'genre']
    list_filter = ['is_active']
    prepopulated_fields = {'slug': ('title',)}


@admin.register(Movie)
class MovieAdmin(admin.ModelAdmin):
    list_display = ['title', 'director', 'slug', 'genre_1', 'genre_2', 'genre_3',
                    'duration']
    list_filter = ['is_active']
    list_editable = ['duration']
    prepopulated_fields = {'slug': ('title',)}


@admin.register(CD)
class CDAdmin(admin.ModelAdmin):
    list_display = ['title', 'band', 'slug', 'genre_1', 'genre_2',
                    'music_list']
    list_filter = ['is_active']
    list_editable = ['music_list']
    prepopulated_fields = {'slug': ('title',)}


@admin.register(Rent)
class RentAdmin(admin.ModelAdmin):
    list_display = ['user', 'depositet_book', 'depositet_movie', 'depositet_cd', 'deposit_date', 'deposit_length']
