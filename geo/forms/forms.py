from django import forms
from .models import Forms,  Division, Subdivision, SubdivisionDetail, Files, Comment

from django.db.models import Sum


class FormForm(forms.ModelForm):

    class Meta:
        model = Forms
        fields = ('type_of_accreditation',  'year',
                  'created_for', 'is_active')


class SubdivisionForm(forms.ModelForm):

    class Meta:
        model = Subdivision
        fields = ('criteria', )
        labels = {"Points": "Weight", 'subtotal': 'Total'}
        widgets = {
            'criteria':  forms.Textarea(attrs={}),
            'Points': forms.NumberInput(attrs={'style': 'width:100pt'}),
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
                  )
        labels = {'subdivisiondetail': 'For Subcriteria',
                  }


class DivisionForm(forms.ModelForm):

    class Meta:
        model = Division
        fields = ('criteria',)

        widgets = {
            'criteria': forms.Textarea(attrs={'class': 'special', 'maxlength': '99', }),



        }


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('comment',)
        labels = {'comment': 'Add comment',
                  }
