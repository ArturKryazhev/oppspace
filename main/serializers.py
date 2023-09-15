from rest_framework import serializers
from .models import *

class Contact_usSerializer(serializers.ModelSerializer):
    class Meta:
        model = Contact_us
        fields = '__all__'

class NotificationsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Notifications
        fields = '__all__'