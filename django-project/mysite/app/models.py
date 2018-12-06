from django.db import models

# Create your models here.


class Photo(models.Model):
    name = models.CharField(max_length=100)
    creator = models.CharField(max_length=100)
    price = models.CharField(max_length=100)

    def __str__(self):
        """ Change representation of object """
        return self.name + '-' + self.creator