from django.db import models
from django.urls import reverse

# Create your models here.


class Book(models.Model):
    name = models.CharField(max_length=100)
    author = models.CharField(max_length=100)
    price = models.CharField(max_length=100)
    category = models.CharField(max_length=100, default='drama')

    def __str__(self):
        """ Change representation of object """
        return self.name + '-' + self.author

    def get_absolute_url(self):
        return reverse('books:detail', kwargs={'pk': self.pk})