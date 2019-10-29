from django.shortcuts import render


def index(request):
    return render(request, 'mapMain.html')
# Create your views here.
