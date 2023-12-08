from django.db import models
from django.urls import reverse


class Menu(models.Model):
    title = models.CharField(
        max_length=256, unique=True, verbose_name='Название меню')
    slug = models.SlugField(
        max_length=256, unique=True, verbose_name='Слаг меню')

    class Meta:
        verbose_name = 'меню'
        verbose_name_plural = 'Меню'

    def __str__(self):
        return self.title


class Item(models.Model):
    title = models.CharField(max_length=256, verbose_name='Название предмета')
    slug = models.SlugField(
        max_length=256, unique=True, verbose_name='Слаг предмета')
    menu = models.ForeignKey(
        Menu, blank=True, related_name='items', on_delete=models.CASCADE)
    parent = models.ForeignKey(
        'self',
        blank=True,
        null=True,
        related_name='childrens',
        on_delete=models.CASCADE
        )

    class Meta:
        verbose_name = 'предмет меню'
        verbose_name_plural = 'Предметы меню'

    def __str__(self):
        return self.title
