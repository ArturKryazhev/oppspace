from django.shortcuts import render
from .models import *
from .forms import *

def briefs(request):
    form = EcommerceForm(request.POST)
    if request.method == 'POST':
        
        if form.is_valid():
            form.save()
    context = {'form': form}
    return render(request, 'brief/brief.html', context)
# Create your views here.
