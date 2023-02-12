from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import User

class UserCreationForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        model = User
        fields = UserCreationForm.Meta.fields + ('name', 'dob','highest_qualification','contact')


class UserProfileForm(forms.ModelForm):
    class Meta:
        model = User
        fields = [ 'name','dp','dob', 'highest_qualification','resume']
        widgets = {
            'dp': forms.ClearableFileInput(attrs={'multiple': False})
        }
