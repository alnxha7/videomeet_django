from django.shortcuts import render

def index(request):
    return render(request, 'index.html')

def live(request):
    return render(request, 'live.html')

