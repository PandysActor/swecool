from django.shortcuts import render
from django.http import HttpResponse


# Create your views here

def home(request):
    return render(request, 'landingspage.html')

# Hier zet je nog meer views
