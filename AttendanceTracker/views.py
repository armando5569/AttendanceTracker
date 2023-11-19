from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
import secrets
import string
from django.shortcuts import render, redirect



#app function pages
@login_required
def confirmation(request):
    return render(request, 'attendancetracker/confirmation.html')

@login_required
def courses(request):
    return render(request, 'attendancetracker/courses.html')

@login_required
def editcourse(request):
    return render(request, 'attendancetracker/editcourse.html')

@login_required
def reports(request):
    return render(request, 'attendancetracker/reports.html')

@login_required
def absent_view(request):
    return render(request, 'attendancetracker/absent.html')

@login_required
def startclass(request):
    if request.method == 'POST':
        # Generate a random code
        code = ''.join(secrets.choice(string.ascii_uppercase + string.digits) for _ in range(6))

        # Render the template with the generated code and a message
        return render(request, 'attendancetracker/startclass.html', {'code': code, 'message': 'Class started. Share this code with your students.'})

    return render(request, 'attendancetracker/startclass.html', {'code': None, 'message': None})

@login_required
def add_course(request):
    if request.method == 'POST':
        # Process form data for adding a new course
        # ...

        # Redirect to a confirmation page or another appropriate view
        return redirect('confirmation')

    return render(request, 'attendancetracker/courses.html')

@login_required
def update_course(request):
    if request.method == 'POST':
        # Process form data for updating an existing course
        # ...

        # Redirect to a confirmation page or another appropriate view
        return redirect('confirmation')

    return render(request, 'attendancetracker/courses.html')

