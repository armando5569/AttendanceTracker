from django.shortcuts import render
from django.http import HttpResponse


#app function pages
def confirmation(request):
    return render(request, 'attendancetracker/confirmation.html')

def courses(request):
    return render(request, 'attendancetracker/courses.html')

def editcourse(request):
    return render(request, 'attendancetracker/editcourse.html')

def reports(request):
    return render(request, 'attendancetracker/reports.html')

def startclass(request):
    return startclass(request, 'attendancetracker/startclass.html')