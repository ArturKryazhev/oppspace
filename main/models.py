from django.db import models

class Contact_us(models.Model):
    name = models.CharField(max_length=255, verbose_name='Имя')
    telephone = models.CharField(max_length=25, verbose_name='телефон')
    e_mail = models.EmailField(verbose_name='E-mail')
    task = models.CharField(max_length=255, verbose_name='Ваша задача')
    text_message = models.TextField(verbose_name='текст сообщения')

class Notifications(models.Model):
    e_mail = models.EmailField(verbose_name='E-mail')

class Employee(models.Model):
    second_name = models.CharField(max_length=255, verbose_name='Фамилия')
    name = models.CharField(max_length=255, verbose_name='Имя')
    father_name = models.CharField(max_length=255, verbose_name='Отчество', blank= True, null= True)
    photo = models.ImageField()
    description = models.TextField(verbose_name='Описание работы')
    photo = models.ImageField(verbose_name='Фотография')
    education = models.CharField(max_length=255, verbose_name='Образование')
    date_education = models.CharField(max_length=4, verbose_name='Дата окончания образования')
    experience = models.CharField(max_length=50, verbose_name='Опыт работы')
    place_work = models.CharField(max_length=255, verbose_name='Место работы')
    work_address = models.CharField(max_length=255, verbose_name='Адрес работы')
# Create your models here.
