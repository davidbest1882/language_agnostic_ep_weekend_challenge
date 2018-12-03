from django.shortcuts import render
from .models import Peep

def home(request):
    context = {
        'peeps': Peep.objects.all()
    }
    return render(request, 'chitter/home.html', context)

def about(request):
    return render(request, 'chitter/about.html', {'title': 'About'})
