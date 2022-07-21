from django.shortcuts import render
from .models import Books, Movies, Music, Games

# Create your views here.
def main(request):
    data = {}
    return render(request, "main.html", context=data) 

def books(request):
    knigi = Books.objects.all()
    data = {"knigi":knigi}
    return render(request, "books.html", context=data) 

def movies(request):
    films = Movies.objects.all()
    data = {"films":films}
    return render(request, "movies.html", context=data) 

def music(request):
    albums = Music.objects.all()
    data = {"albums":albums}
    return render(request, "music.html", context=data) 

def games(request):
    igry = Games.objects.all()
    data = {"igry":igry}
    return render(request, "games.html", context=data) 