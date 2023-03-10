from  django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from stack.models  import Questions,Userprofile

class RegistrationForm(UserCreationForm):
    
    class Meta:
        model=User
        fields=["username","email","password1","password2"]


class LoginForm(forms.Form):
    username=forms.CharField()
    password=forms.CharField(widget=forms.PasswordInput())
class QuestionForm(forms.ModelForm):
    class Meta:
        model=Questions
        fields=["description","image"]


class UserprofileForm(forms.ModelForm):
    class Meta:
        model=Userprofile
        fields=["profile_pic","bio"]
