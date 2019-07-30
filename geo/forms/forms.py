from django import forms
from .models import CreateForm

class CreateForm_FORMs(forms.ModelForm):
    class Meta:
        model=CreateForm
        fields = '__all__'