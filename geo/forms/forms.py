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
            'points': forms.NumberInput(attrs={'style': 'width:100pt'}),
        }


class SubdivisionDetailForm(forms.ModelForm):

    class Meta:
        model = SubdivisionDetail

        fields = ('criteria',  'subpoints',
                  'remarks', 'subtotal')

        labels = {"subpoints": "Breakdown", 'subtotal': 'Subpoints'}
        widgets = {
            'criteria':  forms.Textarea(attrs={'style': 'width:150pt'}),

            'subpoints': forms.NumberInput(attrs={'style': 'width:100pt'}),
            'remarks':  forms.Textarea(attrs={'style': 'width:150pt'}),
            'subtotal': forms.NumberInput(attrs={'style': 'width:100pt'}),

        }


class FileForm(forms.ModelForm):
    class Meta:
        model = Files
        fields = ('subdivisiondetail', 'filename', 'file')
        labels = {'subdivisiondetail': 'For Subcriteria'}


class DivisionForm(forms.ModelForm):

    class Meta:
        model = Division
        fields = ('criteria',)

        widgets = {
            'criteria': forms.Textarea(attrs={'class': 'special', 'maxlength': '99', }),



        }
