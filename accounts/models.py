from django.db import models
from django.contrib.auth.models import AbstractUser
import uuid

class User(AbstractUser):
    class Role(models.IntegerChoices):
        STUDENT = 1
        TEACHER = 2
        ADMINISTRATOR = 3

    base_role = Role.STUDENT

    userID = models.AutoField(primary_key=True, unique=True, editable=False)
    roleID = models.IntegerField(choices=Role.choices, default=base_role)

    
    def getRole(self):
        return self.role


class Course(models.Model):
    courseID = models.CharField(max_length=16, primary_key=True)
    courseName = models.CharField(max_length=32)
    
    def __str__(self):
        return self.courseID


class Section(models.Model):
    sectionID = models.IntegerField(primary_key=True)
    def __str__(self):
        return str(self.sectionID)


class Classes(models.Model):
    classID = models.UUIDField(primary_key=True, editable=False, default=uuid.uuid4)
    courseID = models.ForeignKey(Course, on_delete=models.CASCADE, related_name="ClassCourseID")
    sectionID = models.ForeignKey(Section, on_delete=models.CASCADE, related_name="ClassSectionID")
    checkincode = models.CharField(max_length=6, blank=True, null=True)
    starttime = models.DateField(auto_now_add=True)
    endtime = models.DateField(auto_now_add=False, null=True)


class Enrollment(models.Model):
    enrollmentID = models.UUIDField(primary_key=True,editable=False, default=uuid.uuid4) 
    userID = models.ForeignKey(User, on_delete=models.CASCADE, related_name="EnrollUserID")
    courseID = models.ForeignKey(Course, on_delete=models.CASCADE, related_name="EnrollCourseID")
    sectionID = models.ForeignKey(Section, on_delete=models.CASCADE, related_name="EnrollSectionID")


class TeacherAssignment(models.Model):
    assignmentID = models.UUIDField(primary_key=True, editable=False, default=uuid.uuid4)
    userID = models.ForeignKey(User, on_delete=models.CASCADE, related_name="TAuserID")
    courseID = models.ForeignKey(Course, on_delete=models.CASCADE, related_name="TAcourseID")
    sectionID = models.ForeignKey(Section, on_delete=models.CASCADE, related_name="TAsectionID") 


class Attendance(models.Model):
    attendanceID = models.UUIDField(primary_key=True, editable=False, default=uuid.uuid4)
    userID = models.ForeignKey(User, on_delete=models.CASCADE, related_name="AttendanceUserID")
    classID = models.ForeignKey(Classes, on_delete=models.CASCADE, related_name="AttendanceClassID")
    checkintime = models.DateField(auto_now_add=True)

