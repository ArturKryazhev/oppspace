from django.shortcuts import render,redirect
from .models import *
from .forms import *

def briefs(request):
    form = EcommerceForm(request.POST)
    if request.method == 'POST':
        if form.is_valid():
            form.save()
        return redirect('main:main_page')
    context = {'form': form}
    return render(request, 'brief/brief.html', context)
# Create your views here.
