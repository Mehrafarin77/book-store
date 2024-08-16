from .models import *
from django.forms import ModelForm

class BookForm(ModelForm):
    class Meta:
        model = Book
        fields = ['title', 'rating', 'author', 'is_bestselling', 'published_countries']

class AuthorForm(ModelForm):
    class Meta:
        model = Author
        fields = ['first_name', 'last_name', 'address']


class AddressForm(ModelForm):
    class Meta:
        model = Address
        fields = ['street', 'postal_code', 'city']


class CountryForm(ModelForm):
    class Meta:
        model = Country
        fields = ['name', 'code']
