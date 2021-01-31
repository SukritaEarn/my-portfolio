from django import forms

from .models import Contact

class ContactForm(forms.ModelForm):
    class Meta:
        model = Contact
        fields = ['name', 'email', 'message']
        widgets = {
            'name': forms.TextInput(attrs={'class':'form-control'}),
            'email': forms.TextInput(attrs={'class':'form-control', 'type':'email'}),
            'message': forms.Textarea(attrs={'class':'form-control','rows':8})
        }
