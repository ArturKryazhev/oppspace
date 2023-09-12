# Generated by Django 4.2.5 on 2023-09-11 18:37

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Contact_us',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255, verbose_name='Имя')),
                ('telephone', models.CharField(max_length=25, verbose_name='телефон')),
                ('e_mail', models.EmailField(max_length=254, verbose_name='E-mail')),
                ('task', models.CharField(max_length=255, verbose_name='Ваша задача')),
                ('text_message', models.TextField(verbose_name='текст сообщения')),
            ],
        ),
        migrations.CreateModel(
            name='Notifications',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('e_mail', models.EmailField(max_length=254, verbose_name='E-mail')),
            ],
        ),
    ]