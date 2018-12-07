from django.urls import path
from bookapp import views

app_name = 'books'

urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),
    path('<int:pk>/', views.DetailView.as_view(), name='detail'),
    path('books/add/', views.BookCreate.as_view(), name='book-add'),
]
