from django import forms
from .models import Division, Subdivision, SubdivisionDetail


class SubdivisionForm(forms.ModelForm):

    class Meta:
        model = Subdivision
        fields = "__all__"
