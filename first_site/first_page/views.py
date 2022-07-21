from django.shortcuts import render
from django.http import HttpResponse
# from .models import Books

# Create your views here.
# нужно создать функцию, которая в себя получит запрос
def floppa(request):
    # Django по запросу request достает шаблон index из папки templates
    # с помощью атрибута context можно наполнять страницу данными
    # лучше сначала создать словарь данных
    data = {
        # сначала название переменной, потом значение переменной
        "floppa_h1":"Большой шлёпа",
        "floppa_p":"Русский кот"
    }
    return render(request, "floppa.html", context=data)

# функция для главного рута
def hello(request):
    return HttpResponse('<center><a href="floppa/" style="color: red; font-size: 48px; text-decoration: none;">Большой шлёпа</a><br><a href="media/" style="color: red; font-size: 48px; text-decoration: none;">Энциклопедия медиа</a></center>')

def pelmeni(request): # функцию для показывания новой страницы
    data = {
        "pelmeni_h2": "Хорошие пельмени — это очень-очень вкусно. На самом деле рецепт простой: много мяса, мало теста"
    }
    return render(request, "pelmeni.html", context=data)

# def books(request):
#     books = Books.objects.all()
#     return render(request, "books.html", context={"books":books, "title":"Книги"})