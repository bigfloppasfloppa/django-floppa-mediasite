"""first_site URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from first_page.views import hello, floppa, pelmeni #, books
from mediasite.views import main, books, movies, music, games

urlpatterns = [
    path('admin/', admin.site.urls),
    # мы можем добавлять сколько угодно адресов
    path('', hello),
    path('floppa/', floppa),
    path('pelmeni/', pelmeni),
    # path('books/', books),
    path('media/', main),
    path('media/books', books),
    path('media/movies', movies),
    path('media/music', music),
    path('media/games', games),

]
