from django.shortcuts import render,redirect
from django.http import HttpResponse

# Create your views here.
#Homepage
def about(request):
    return render(request, '1.html')
def Home(request):
    return render(request, '2.html')
def contactus(request):
    return render(request, '3.html')