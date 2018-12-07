from django.shortcuts import render
from django.http import Http404
from .models import Photo

# Create your views here.

def index(req): 
    all_photos = Photo.objects.all()
    return render(req, 'app/index.html', {'all_photos': all_photos}) 

def detail(req, photo_id):
    try:
        photo = Photo.objects.get(id = photo_id)
    except Photo.DoesNotExist:
        raise Http404('Photo not found')

    return render(req, 'app/detail.html', {'photo': photo})