from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required

from accounts.models import *
from .forms import *

import secrets
import string



#app function pages

#
# for all users 
#

@login_required
def confirmation(request):
    return render(request, 'attendancetracker/confirmation.html')

@login_required
#page shows the options for creating a report
def reports(request):
    return render(request, 'attendancetracker/reports.html')

@login_required
def absent_view(request):
    return render(request, 'attendancetracker/absent.html')

#
# for administrators only 
#

@login_required
# page shows the list of courses. 
def courses(request):
    context ={}
 
    # add the dictionary during initialization
    context["Courses"] = Course.objects.all()
    return render(request, 'attendancetracker/courses.html', context)

@login_required
#page shows the form to add/edit courses. 
def editcourse(request):
    courseContent = {}
    form = CourseForm(request.POST or None)
    if form.is_valid():
        form.save()
    courseContent['form']= form
    return render(request, 'attendancetracker/editcourse.html', courseContent)

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


#
# for teachers only 
#

@login_required
def startclass(request):
    if request.method == 'POST':
        # Generate a random code
        code = ''.join(secrets.choice(string.ascii_uppercase + string.digits) for _ in range(6))

        # Render the template with the generated code and a message
        return render(request, 'attendancetracker/startclass.html', {'code': code, 'message': 'Class started. Share this code with your students.'})

    return render(request, 'attendancetracker/startclass.html', {'code': None, 'message': None})

#
# for students only 
#

def process_code(request):
    if request.method == 'POST':
        entered_code = request.POST.get('code', '')
        # Perform validation or check the entered code against your database
        # If the code is valid, redirect to the specific template
        if is_valid_code(entered_code):
            return redirect('attendancetracker/confirmation.html')
        else:
            # Code is invalid, you may want to show an error message
            return render(request, 'attendancetracker/studcode.html', {'error': 'Invalid code'})
    else:
        # Handle GET requests to this view
        return render(request, 'attendancetracker/studcode.html')

def is_valid_code(code):
    # Implement your validation logic here (e.g., check against the database)
    # Return True if the code is valid, False otherwise
    return code == '123456'  # Replace with your actual validation logic

