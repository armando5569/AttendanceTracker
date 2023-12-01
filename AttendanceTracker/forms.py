from django import forms
from accounts.models import *

class CourseForm(forms.ModelForm):
    class Meta:
        model = Course

        fields = [
            "courseID",
            "courseName"
        ]
