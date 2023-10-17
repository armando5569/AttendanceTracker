from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def home(request):
    return render(request, 'attendancetracker/home.html')

def signup(request):
    return render(request, 'attendancetracker/signup.html')

def login(request):
    return render(request, 'attendancetracker/login.html')
