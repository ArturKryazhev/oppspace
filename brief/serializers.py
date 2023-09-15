from rest_framework import serializers
from .models import *

class BriefSerializer(serializers.ModelSerializer):
    class Meta:
        model = Ecommerce
        fields = "__all__"
