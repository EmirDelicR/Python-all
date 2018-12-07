from django.views import generic
from django.views.generic.edit import CreateView
from .models import Book

# Create your views here.

class IndexView(generic.ListView):
    template_name = 'bookapp/index.html'

    def get_queryset(self): 
        return Book.objects.all()


class DetailView(generic.DetailView):
    model = Book
    template_name = 'bookapp/detail.html'


class BookCreate(CreateView):
    model = Book
    fields = ['name', 'author', 'price', 'category']
