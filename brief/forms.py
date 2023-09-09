from django import forms
from .models import *

class EcommerceForm(forms.ModelForm):
    class Meta:
        model = Ecommerce
        fields = "__all__"
