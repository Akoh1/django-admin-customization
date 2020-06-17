from django import forms
from .models import TestUser

class TestUserform(forms.ModelForm):    

    class Meta:
        model= TestUser
        fields= ['username', 'email', 'gender']