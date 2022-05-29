from django.shortcuts import render
from django.shortcuts import get_object_or_404, render
from django.http import HttpResponse
from django.urls import reverse, reverse_lazy
from django.views import generic
from .forms import PostForm_book
from django.core.exceptions import ValidationError, PermissionDenied
from django.contrib.auth.models import User
from django.contrib.auth.mixins import LoginRequiredMixin

from .models import Category, Book, CD, Movie, Rent


class IndexView(generic.ListView):
    model = Category
    template_name = 'repository/index.html'


class CategoryBookView(generic.ListView):
    model = Book
    template_name = 'repository/category_index_book.html'


class CategoryMovieView(generic.ListView):
    model = Movie
    template_name = 'repository/category_index_movie.html'

#    def get_queryset(self):
#        return Book.ordering('-created')[:5]


class CategoryCDView(generic.ListView):
    model = CD
    template_name = 'repository/category_index_cd.html'


class SingleView_book(generic.DetailView):
    model = Book
    template_name = 'repository/single_book.html'
    context_object_name = 'book'


class SingleView_movie(generic.DetailView):
    model = Movie
    template_name = 'repository/single_movie.html'
    context_object_name = 'movie'


class SingleView_cd(generic.DetailView):
    model = CD
    template_name = 'repository/single_cd.html'
    context_object_name = 'cd'


class AddView_book(LoginRequiredMixin, generic.CreateView):
    template_name = 'repository/add.html'
    model = Book
    fields = '__all__'
    success_url = reverse_lazy('repository:index')


class AddView_movie(LoginRequiredMixin, generic.CreateView):
    model = Movie
    template_name = 'repository/add.html'
    fields = '__all__'
    success_url = reverse_lazy('repository:index')


class AddView_cd(LoginRequiredMixin, generic.CreateView):
    model = CD
    template_name = 'repository/add.html'
    fields = '__all__'
    success_url = reverse_lazy('repository:index')


class EditView_book(LoginRequiredMixin, generic.UpdateView):
    model = Book
    template_name = 'repository/edit.html'
    fields = '__all__'
    pk_url_kwarg = 'pk'
    success_url = reverse_lazy('repository:index')


class EditView_movie(LoginRequiredMixin, generic.UpdateView):
    model = Movie
    template_name = 'repository/edit.html'
    fields = '__all__'
    pk_url_kwarg = 'pk'
    success_url = reverse_lazy('repository:index')


class EditView_cd(LoginRequiredMixin, generic.UpdateView):
    model = CD
    template_name = 'repository/edit.html'
    fields = '__all__'
    pk_url_kwarg = 'pk'
    success_url = reverse_lazy('repository:index')


class DeleteView_book(LoginRequiredMixin, generic.DeleteView):
    model = Book
    pk_url_kwarg = 'pk'
    success_url = reverse_lazy('repository:index')
    template_name = 'repository/delete.html'


class DeleteView_movie(LoginRequiredMixin, generic.DeleteView):
    model = Movie
    pk_url_kwarg = 'pk'
    success_url = reverse_lazy('repository:index')
    template_name = 'repository/delete.html'


class DeleteView_cd(LoginRequiredMixin, generic.DeleteView):
    model = CD
    pk_url_kwarg = 'pk'
    success_url = reverse_lazy('repository:index')
    template_name = 'repository/delete.html'


class Deposite(LoginRequiredMixin, generic.CreateView):
    model = Rent
    fields = '__all__'
    success_url = reverse_lazy('repository:index')
    template_name = 'repository/edit.html'


class Deposite_delete(LoginRequiredMixin, generic.DeleteView):
    model = Rent
    fields = '__all__'
    success_url = reverse_lazy('repository:index')
    template_name = 'repository/delete.html'


class Statistics(generic.ListView):
    model = Rent
    pk_url_kwarg = 'pk'
    template_name = 'repository/statistics.html'
    context_object_name = 'rents'
