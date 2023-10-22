from datetime import date
from django.db import models


class Country(models.Model):
    class Meta:
        verbose_name = "Страна"
        verbose_name_plural = "Страны"
    name = models.CharField(max_length=255,verbose_name="Имя")

    def __str__(self):
        return f'{self.name}'


class Producter(models.Model):
    class Meta:
        verbose_name = "Производитель"
        verbose_name_plural = "Производители"

    name = models.CharField(max_length=255,  verbose_name="Имя")
    country = models.ForeignKey('Country', on_delete=models.CASCADE, verbose_name="Страна", related_name='producters')

    def __str__(self):
        return f'{self.name}'


class Car(models.Model):
    class Meta:
        verbose_name = "Автомобиль"
        verbose_name_plural = "Автомобили"
    name = models.CharField(max_length=255, verbose_name="Имя")
    producter = models.ForeignKey('Producter', on_delete=models.CASCADE, verbose_name="Производитель", related_name='cars')
    start_year = models.IntegerField(verbose_name="Год начала выпуска")
    last_year = models.IntegerField(verbose_name="Год оконания выпуска")

    def __str__(self):
        return f'{self.name}'

class Comment(models.Model):
    class Meta:
        verbose_name = "Комментарий"
        verbose_name_plural = "Комментарии"
    author_email = models.EmailField(verbose_name="Email автора")
    car = models.ForeignKey('Car', on_delete=models.CASCADE, verbose_name = "Автомобиль", related_name='comments')
    date_created = models.DateField(default=date.today, verbose_name="Дата создания")
    text = models.CharField(max_length=512, verbose_name="Комментарий")

    def __str__(self):
        return f'{self.text}'