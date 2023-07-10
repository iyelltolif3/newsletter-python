from django import forms
from .models import newslettersUser

class newsletterUserSingUpForm(forms.Form):
    class meta:
        model = newslettersUser
        fields = ['email']

class newsletterCreationForm(forms.ModelForm):
    class meta:
        model = newslettersUser
        fields = ['name', 'subjet', 'body', 'email']