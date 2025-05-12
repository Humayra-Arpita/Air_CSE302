from django.forms import ModelForm
from django import forms
from .models import *


class PropertyForm(ModelForm):
   class Meta:
       model = Property
       fields = '__all__'

class ProfileForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        fields = ['profile_picture', 'phone_number', 'nid_number']
