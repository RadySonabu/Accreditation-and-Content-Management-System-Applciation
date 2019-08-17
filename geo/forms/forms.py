from django import forms
from .models import Forms,  Division, Subdivision, SubdivisionDetail


class FormForm(forms.ModelForm):

    class Meta:
        model = Forms
        fields = ('title', 'form_type', 'branch', 'year', 'college', 'address',
                  'first_name', 'middle_initial', 'last_name', 'created_for')


class SubdivisionForm(forms.ModelForm):

    class Meta:
        model = Subdivision
        fields = ('criteria', 'points')
        widgets = {
            'criteria': forms.TextInput(attrs={}),
            'points': forms.NumberInput(attrs={'style': 'width:6ch'}),
        }


class SubdivisionDetailForm(forms.ModelForm):

    class Meta:
        model = SubdivisionDetail

        fields = ('criteria',  'subpoints',
                  'remarks', 'subtotal')
        widgets = {
            'criteria': forms.TextInput(attrs={}),
            
            'subpoints': forms.NumberInput(attrs={'style': 'width:6ch'}),
            'remarks': forms.TextInput(attrs={}),
            'subtotal': forms.NumberInput(attrs={'style': 'width:6ch'}),
            
        }
