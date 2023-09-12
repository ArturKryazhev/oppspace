from django.db import models

class Contact_us(models.Model):
    name = models.CharField(max_length=255, verbose_name='Имя')
    telephone = models.CharField(max_length=25, verbose_name='телефон')
    e_mail = models.EmailField(verbose_name='E-mail')
    task = models.CharField(max_length=255, verbose_name='Ваша задача')
    text_message = models.TextField(verbose_name='текст сообщения')

class Notifications(models.Model):
    e_mail = models.EmailField(verbose_name='E-mail')
# Create your models here.
