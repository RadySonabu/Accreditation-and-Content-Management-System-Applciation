from django import forms

from .models import Forms


class FormForm(forms.ModelForm):

    class Meta:
        model = Forms
        fields = "__all__"
