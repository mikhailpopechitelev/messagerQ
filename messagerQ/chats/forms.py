from django import forms 
from .models import *

class AuthorizationForm(forms.ModelForm):
    class Meta:
        model = Autorizations
        fields = ['username','password']
        
        
class RegistrationUser(forms.ModelForm):
       
    class Meta:
        model = Autorizations
        fields = ['username','password']
        
