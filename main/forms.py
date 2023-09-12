from django.forms import ModelForm, TextInput
from .models import *

class ContactUsForm(ModelForm):
    class Meta:
        model = Contact_us
        fields = '__all__'

        widgets = {
            'name': TextInput(attrs={'placeholder': 'Имя'}),
            'telephone': TextInput(attrs={'placeholder': 'Телефон'}),
            'e_mail': TextInput(attrs={'placeholder': 'E-mail'}),
            'task': TextInput(attrs={'placeholder': 'Ваша задача'}),
            'text_message': TextInput(attrs={'placeholder': 'Текст сообщения'})
        }

class NotificationsForm(ModelForm):
    class Meta:
        model = Notifications
        fields = '__all__'

        widgets = {'e_mail': TextInput(attrs={'placeholder': 'E-mail'})}