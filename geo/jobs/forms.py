from django import forms
from .models import BuyerJobBuyerA00,BuyerJobBuyerA01,BuyerJobBuyerA02,BuyerJobBuyerA03,JobJobA00,JobJobA01,ProviderJobProviderA00,ProviderJobProviderA01


class BuyerA00Form(forms.ModelForm):
    class Meta:
        model = BuyerJobBuyerA00
        fields = "__all__"

class BuyerA01Form(forms.ModelForm):
    class Meta:
        model = BuyerJobBuyerA01
        fields = "__all__"

class BuyerA02Form(forms.ModelForm):
    class Meta:
        model = BuyerJobBuyerA02
        fields = "__all__"

class BuyerA03Form(forms.ModelForm):
    class Meta:
        model = BuyerJobBuyerA03
        fields = "__all__"