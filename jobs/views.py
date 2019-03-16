from django.shortcuts import render

from .models import Job

def home(request):
    jobs = Job.objects    # get all objects from DB
    return render(request,'jobs/home.html', {'jobs':jobs})
