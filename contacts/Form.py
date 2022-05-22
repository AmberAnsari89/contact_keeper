from django import forms
from .models import contact

class saveContact(forms.ModelForm):
    class Meta:
        model=contact
        fields=['name','address','phone', 'email','contact_type']
