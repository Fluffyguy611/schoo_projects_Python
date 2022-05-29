from django import forms
from django.core import validators
from repository.models import Book, Movie, CD
from django.contrib.auth.models import User


class PostForm_book(forms.ModelForm):
    class Meta:
        model = Book
        fields = '__all__'

    def clean(self):
        super(PostForm_book, self).clean()
        author = self.cleaned_data.get('author')
        title = self.cleaned_data.get('title')
        genre = self.cleaned_data.get('genre')
        authors_list = Book.objects.filter(author='author')
        if author == authors_list:
            raise validators.ValidationError("Author already exists")
        return self.cleaned_data


class PostForm_movie(forms.ModelForm):
    class Meta:
        model = Movie
        fields = '__all__'


class PostForm_cd(forms.ModelForm):
    class Meta:
        model = CD
        fields = '__all__'


