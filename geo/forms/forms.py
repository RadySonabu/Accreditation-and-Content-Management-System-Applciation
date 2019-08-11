from django import forms
from .models import Division, Subdivision, SubdivisionDetail


class SubdivisionForm(forms.ModelForm):

    class Meta:
        model = Subdivision
        fields = '__all__'
        widgets = {
            'criteria': forms.TextInput(attrs={}),
            'points': forms.NumberInput(attrs={'style': 'width:6ch'}),
        }


class SubdivisionDetailForm(forms.ModelForm):

    class Meta:
        model = SubdivisionDetail

        fields = ('criteria', 'points', 'subpoints',
                  'remarks', 'subtotal', 'total')
        widgets = {
            'criteria': forms.TextInput(attrs={}),
            'points': forms.NumberInput(attrs={'style': 'width:6ch'}),
            'subpoints': forms.NumberInput(attrs={'style': 'width:6ch'}),
            'remarks': forms.TextInput(attrs={}),
            'subtotal': forms.NumberInput(attrs={'style': 'width:6ch'}),
            'total': forms.NumberInput(attrs={'style': 'width:6ch'}),
        }
