from django.shortcuts import render,redirect
from .models import *
from .forms import *
from rest_framework import generics
from .serializers import *
from rest_framework.viewsets import ModelViewSet
def briefs(request):
    form = EcommerceForm(request.POST, request.FILES)
    if request.method == 'POST':
        if form.is_valid():
            form.save()
        return redirect('main:main_page')
    context = {'form': form}
    return render(request, 'brief/brief.html', context)

def test(request):
    form = testform(request.POST, request.FILES)
    if request.method == 'POST':
        if form.is_valid():
            form.save()
        return redirect('main:main_page')
    context = {'form': form}
    return render(request, 'brief/test.html', context)

class BriefViewSet(ModelViewSet):
    queryset = Ecommerce.objects.all()
    serializer_class = BriefSerializer
# Create your views here.
