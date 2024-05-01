from django.shortcuts import render
from .models import *
# Create your views here.
def home(request):
    views = {}
    delay = 0
    #for experiences section
    views['experiences'] = Experiences.objects.all()

    #for projects section
    views['projects'] = Projects.objects.all()


    # contact post method
    if request.method =='POST':
        name = request.POST['name']
        email = request.POST['email']
        message = request.POST['message']
        phone = request.POST['phone']
        data = Contact.objects.create(
            name = name,
            email = email,
            message = message,
            phone = phone,
        )
        data.save()

    # delay for experiences section
    def update_delay(delay):
        delay=delay + .2
        return delay
    return render(request , 'index.html' , views)

