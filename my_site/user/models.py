from django.db import models
from django.template.base import kwarg_re
from django.urls import reverse

# Create your models here.

class User(models.Model):
    name = models.CharField(max_length=25, verbose_name='Имя')
    slug = models.SlugField(max_length=255, unique=True, db_index=True, verbose_name='URL')
    patronymic = models.CharField(max_length=30, verbose_name='Отчество')
    surname = models.CharField(max_length=35, verbose_name='Фамилия')
    sex = models.CharField(max_length=10, verbose_name='Пол')
    autobiography = models.TextField(blank=True, verbose_name='Автобиография')
    photo = models.ImageField(upload_to='photo/%Y/%m/%d/', verbose_name='Фото')
    time_create = models.DateTimeField(auto_now_add=True, verbose_name='Дата создания')
    time_update = models.DateTimeField(auto_now=True, verbose_name='Дата изменения')
    group = models.ForeignKey('Group', on_delete=models.CASCADE, verbose_name='Группа')

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('user_inf', kwargs={'user_slug': self.slug})

    class Meta:
        verbose_name = 'Сотрудники'
        verbose_name_plural = 'Сотрудники'
        ordering = ['time_create', 'name']

class Group(models.Model):
    name = models.CharField(max_length=255, db_index=True, verbose_name='Отдел')
    slug = models.SlugField(max_length=255, unique=True, db_index=True, verbose_name='URL')
    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('group', kwargs={'group_slug': self.slug})

    class Meta:
        verbose_name = 'Отделы'
        verbose_name_plural = 'Отделы'
        ordering = ['id']