from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm

from .models import AppUser

class AppUserCreationForm(UserCreationForm):
    
      class Meta:
            model = AppUser
            fields = ("username", "email")
            
class AppUserChangeForm(UserChangeForm):
      class Meta:
            model = AppUser
            fields = ("username", "email")
            
