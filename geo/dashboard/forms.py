from django import forms


class FilterForm(forms.Form):

    selectedplant = forms.ModelChoiceField(
        queryset=Forms.objects.all(), required=True)
