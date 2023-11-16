from django.contrib import admin
from .models import Section, Enrollment, TeacherAssignment, Attendance, Classes, Course, User
# Register your models here.
admin.site.register(Enrollment)
admin.site.register(TeacherAssignment)
admin.site.register(Attendance)
admin.site.register(Classes)
admin.site.register(Course)
admin.site.register(User)
admin.site.register(Section)