# view created by Armando Sanchez   
from django.shortcuts import render
from django.contrib.auth.forms import UserCreationForm
from accounts.models import User
from django.urls import reverse_lazy
from django.views import generic
 
class NewUserForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        model = User
 
class SignUpView(generic.CreateView):
    form_class = NewUserForm
    success_url = reverse_lazy("login")
    template_name = "registration/signup.html"