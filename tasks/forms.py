from django import forms
from django.forms import ModelForm,widgets
from matplotlib import widgets
from matplotlib.pyplot import text

from .models import *


class taskform(forms.ModelForm):
    class Meta():

        model = task
        fields = '__all__' 
        widgets = {
            'title':forms.TextInput(attrs={'class':'form-control'}),
            'desc':forms.TextInput(attrs={'class':'form-control'}),
            'complete':forms.NullBooleanSelect(attrs={'class':'form-control'}),
            # 'time_created':forms.TextInputs(attrs={'class':'form-control'}),
            
        } 

class Timeform(forms.ModelForm):
    class Meta():
        model = time    
        fields = '__all__'

class Userform(forms.ModelForm):
    class Meta():
        model = User
        fields = '__all__'

    