from django import forms
from .models import ChaiVariety

class ChaiVarietyForm(forms.Form):
   # chai_varity =forms.ModelChoiceField(queryset=ChaiVarity.objects.all, label="Select chai Variety ")

   chai_varity = forms.CharField()