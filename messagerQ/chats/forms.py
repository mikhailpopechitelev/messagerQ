from django import forms 
from .models import *

class AuthorizationForm(forms.ModelForm):
    
    #username = forms.CharField(label='Username', max_length=45, required=True)
    #password = forms.CharField(label='Password', widget=forms.PasswordInput, required=True, max_length=45)
    class Meta:
        model = Autorizations
        fields = ['username','password']
        
class RegistrationUser(forms.ModelForm):
       
    class Meta:
        model = Autorizations
        fields = ['username','password']