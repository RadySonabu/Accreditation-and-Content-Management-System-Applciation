from django import forms
from .models import Forms,  Division, Subdivision, SubdivisionDetail


class FormForm(forms.ModelForm):

    class Meta:
        model = Forms
        fields = ('type_of_accreditation',  'year',
                  'created_for')


class SubdivisionForm(forms.ModelForm):

    class Meta:
        model = Subdivision
        fields = ('criteria', 'points')
        labels = {"points": "Weight", 'subtotal': 'Total'}
        widgets = {
            'criteria': forms.TextInput(attrs={}),
            'points': forms.NumberInput(attrs={'style': 'width:6ch'}),
        }


class SubdivisionDetailForm(forms.ModelForm):

    class Meta:
        model = SubdivisionDetail

        fields = ('criteria',  'subpoints',
                  'remarks', 'subtotal')

        labels = {"subpoints": "Breakdown", 'subtotal': 'Subpoints'}
        widgets = {
            'criteria': forms.TextInput(attrs={}),

            'subpoints': forms.NumberInput(attrs={'style': 'width:6ch'}),
            'remarks': forms.TextInput(attrs={}),
            'subtotal': forms.NumberInput(attrs={'style': 'width:6ch'}),

        }
