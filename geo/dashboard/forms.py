from django import forms



# class FilterForm(forms.Form):

#     selectedplant = forms.ModelChoiceField(
#         queryset=Forms.objects.all(), required=True)


class LockscreenForm(forms.Form):

    class Meta:
        password1 = forms.CharField(
            label='Password', widget=forms.PasswordInput)
        # model = MyUser
        fields = (
            'email', 'password', 'password1 '
        )
