from django.forms import ModelForm
from .models import *


class ProoertyForm(ModelForm):
   class Meta:
       model = Property
       fields = '__all__'
