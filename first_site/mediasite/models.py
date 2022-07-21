from django.db import models

# Create your models here.
# Create your models here.
# модели в Djando хранятся в классах
class Books(models.Model):
    # в Django много готовых типов данных
    title = models.CharField(max_length=150)
    description = models.TextField(blank=True)
    year = models.CharField(max_length=150)
    
    # вывод объектов класса сразу в строчном режиме
    def __str__(self):
        return self.title


class Movies(models.Model):
    title = models.CharField(max_length=150)
    description = models.TextField(blank=True)
    year = models.CharField(max_length=150)

    def __str__(self):
        return self.title


class Music(models.Model):
    title = models.CharField(max_length=150)
    description = models.TextField(blank=True)
    year = models.CharField(max_length=150)

    def __str__(self):
        return self.title

class Games(models.Model):
    title = models.CharField(max_length=150)
    description = models.TextField(blank=True)
    year = models.CharField(max_length=150)

    def __str__(self):
        return self.title
