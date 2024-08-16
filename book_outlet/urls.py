from django.urls import path
from .views import *

app_name = 'book_outlet'
urlpatterns = [
    path('new-book/', add_book, name='add_book'),
    path('new-address/', add_address, name='add_address'),
    path('new-country/', add_country, name='add_country'),
    path('new-author/', add_author, name='add_author'),
    path('', view_books, name='view_books'),
    path('<slug:slug>/', view_book, name='view_book'),
    path('delete/<int:id>', delete_book, name='delete_book'),
    path('edit/<int:id>', edit_book, name='edit_book'),
]