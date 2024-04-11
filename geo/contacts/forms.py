from django import forms
from .models import ContactContactA00, ContactContactA01, ContactContactA02, ContactContactA03,ContactContactA04,ContactGroupA00, ContactGroupA01


class ContactA00Form(forms.ModelForm):

    class Meta:
        model = ContactContactA00
        fields = ['first_name', 'middle_initial', 'last_name', 'email', 'address_1', 'barangay_district', 'city_municipality','postal_code','province','phone_1', 'phone_2']

class ContactA01Form(forms.ModelForm):
    class Meta:
        model = ContactContactA01
        fields = [ 'skill_id','comments', ]

class ContactA02Form(forms.ModelForm):
    class Meta:
        model = ContactContactA02
        fields = ['endorsement_id','message']

class ContactA03Form(forms.ModelForm):
    class Meta:
        model = ContactContactA03
        fields = ['sample_work_id','file_name', 'comments']

class ContactA04Form(forms.ModelForm):
    class Meta:
        model = ContactContactA04
        fields = ['contact_deduction_id','deduction_id_id', 'comments']

class GroupA00Form(forms.ModelForm):
    class Meta:
        model = ContactGroupA00
        fields = ['name', 'email', 'address_1', 'barangay_district', 'city_municipality','postal_code','province','phone_1', 'phone_2', 'agent']

class GroupA01Form(forms.ModelForm):
    class Meta:
        model = ContactGroupA01
        fields = ['group_id','group_role', 'comments']