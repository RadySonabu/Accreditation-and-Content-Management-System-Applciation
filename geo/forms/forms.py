from django import forms
from .models import CoE_IT_FORM
class CoE_IT_FORM_FORMs(forms.ModelForm):
    class Meta:
        model=CoE_IT_FORM
        fields = '__all__'
