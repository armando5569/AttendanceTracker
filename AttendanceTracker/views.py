from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required



#app function pages
def confirmation(request):
    return render(request, 'attendancetracker/confirmation.html')

def courses(request):
    return render(request, 'attendancetracker/courses.html')

def editcourse(request):
    return render(request, 'attendancetracker/editcourse.html')

@login_required
def reports(request):
    return render(request, 'attendancetracker/reports.html')


def startclass(request):
    return startclass(request, 'attendancetracker/startclass.html')