from django.shortcuts import render
from .models import *
# Create your views here.
def home(request):
    views = {}
    delay = 0
    views['experiences'] = Experiences.objects.all()

    def update_delay(delay):
        delay=delay + .2
        return delay
    return render(request , 'index.html' , views)

