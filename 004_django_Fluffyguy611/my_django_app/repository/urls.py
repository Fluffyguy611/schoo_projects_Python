from django.urls import path
import os
from . import views

app_name = 'repository'

urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),
    path('Statistics/', views.Statistics.as_view(), name='statistics'),
    path('rent/', views.Deposite.as_view(), name='rent'),
    path('books/add/', views.AddView_book.as_view(), name='add'),
    path('movies/add/', views.AddView_movie.as_view(), name='add'),
    path('cds/add/', views.AddView_cd.as_view(), name='add'),
    path('books/edit/<int:pk>/', views.EditView_book.as_view(), name='edit_book'),
    path('movies/edit/<int:pk>/', views.EditView_movie.as_view(), name='edit_movie'),
    path('cds/edit/<int:pk>/', views.EditView_cd.as_view(), name='edit_cd'),
    path('books/delete/<int:pk>/', views.DeleteView_book.as_view(), name='delete_book'),
    path('movies/delete/<int:pk>/', views.DeleteView_movie.as_view(), name='delete_movie'),
    path('cds/delete/<int:pk>/', views.DeleteView_cd.as_view(), name='delete_cd'),
    path('books/', views.CategoryBookView.as_view(), name='category_index_book'),
    path('movies/', views.CategoryMovieView.as_view(), name='category_index_movie'),
    path('cds/', views.CategoryCDView.as_view(), name='category_index_cd'),
    path('book/<slug:slug>/', views.SingleView_book.as_view(), name='single_book'),
    path('movie/<slug:slug>/', views.SingleView_movie.as_view(), name='single_movie'),
    path('cd/<slug:slug>/', views.SingleView_cd.as_view(), name='single_cd'),
]