from django.shortcuts import render, redirect
from .models import *
from .forms import *
from rest_framework import generics
from .serializers import *
from rest_framework.viewsets import ModelViewSet

def Forms(request):
    ContactUsform = ContactUsForm(request.POST)
    if request.method == 'POST':
        if ContactUsform.is_valid():
            ContactUsform.save()
        return redirect('main:main_page')
    Notifications_form = NotificationsForm(request.POST)
    if request.method == 'POST':
        if Notifications_form.is_valid():
            Notifications_form.save()
        return redirect('main:main_page')
    context = {'ContactUsform': ContactUsform,
               'Notifications_form':Notifications_form}
    return render(request,'main/main.html',context)

def main_page(request):

    context = {}
    return render(request, 'main/main.html',context)

class Contact_usViewSet(ModelViewSet):
    queryset = Contact_us.objects.all()
    serializer_class = Contact_usSerializer

class NotificationsViewSet(ModelViewSet):
    queryset = Notifications.objects.all()
    serializer_class = NotificationsSerializer


# Create your views here.
