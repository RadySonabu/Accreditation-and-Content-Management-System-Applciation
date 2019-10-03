from django import forms
from .models import Forms,  Division, Subdivision, SubdivisionDetail, Files


class FormForm(forms.ModelForm):

    class Meta:
        model = Forms
        fields = ('type_of_accreditation',  'year',
                  'created_for', 'is_active')


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
                  'remarks', 'subtotal', 'can_upload')

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
        fields = ('subdivisiondetail', 'filename', 'file',
                  'note_from_auditor', 'note_from_audited')
        labels = {'subdivisiondetail': 'For Subcriteria',
                  'note_from_audited': 'My note', 'note_from_auditor': 'Note'}


class DivisionForm(forms.ModelForm):

    class Meta:
        model = Division
        fields = ('criteria',)

        widgets = {
            'criteria': forms.Textarea(attrs={'class': 'special', 'maxlength': '99', }),



        }
