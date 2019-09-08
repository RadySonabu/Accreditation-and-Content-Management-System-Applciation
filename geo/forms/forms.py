from django import forms
from .models import Forms,  Division, Subdivision, SubdivisionDetail, Files


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
            'criteria':  forms.Textarea(attrs={}),
            'points': forms.NumberInput(attrs={'style': 'width:50pt'}),
        }


class SubdivisionDetailForm(forms.ModelForm):

    class Meta:
        model = SubdivisionDetail

        fields = ('criteria',  'subpoints',
                  'remarks', 'subtotal')

        labels = {"subpoints": "Breakdown", 'subtotal': 'Subpoints'}
        widgets = {
            'criteria':  forms.Textarea(attrs={}),

            'subpoints': forms.NumberInput(attrs={'style': 'width:50pt'}),
            'remarks':  forms.Textarea(attrs={}),
            'subtotal': forms.NumberInput(attrs={'style': 'width:50pt'}),

        }


class FileForm(forms.ModelForm):
    class Meta:
        model = Files
        fields = ('title', 'author', 'pdf')


class DivisionForm(forms.ModelForm):

    class Meta:
        model = Division
        fields = ('criteria',)

        widgets = {
            'criteria': forms.Textarea(attrs={'class': 'special', 'maxlength': '99', }),



        }
