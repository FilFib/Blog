from django.shortcuts import render
from .models import BlogPost

def home(request):
    posts = BlogPost.objects.all() # metoda objects jest dziedziczona z klasy model, wyciągamy wszytskie obiekty z tabeli
    return render(request, 'home.html', {'posts': posts})
