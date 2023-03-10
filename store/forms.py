from django.contrib.auth.models import User
from django import forms
from django.contrib.auth.forms import UserCreationForm
class SignUpForm(UserCreationForm):
   frist_name = forms.CharField(max_length=100,required=True)
   last_name = forms.CharField(max_length=100,required=True)
   email = forms.EmailField(max_length=250,help_text='example@gmail.com')

   class Meta :
       model = User
       fields=('frist_name','last_name','username','email','password1','password2')

