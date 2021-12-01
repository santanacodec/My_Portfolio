from django import forms

def should_be_empty(value):
    if value:
        raise forms.ValidationError('Field is not empty')

class ContactForm(forms.Form):
    name = forms.CharField(required=True, widget=forms.TextInput(attrs={'class' : 'form-control', 'placeholder': "Name"}))
    email = forms.EmailField(required = True, widget=forms.EmailInput(attrs={'class' : 'form-control', 'placeholder': "Email"}))
    message = forms.CharField(required = True, widget=forms.Textarea(attrs={'class' : 'form-control', 'placeholder': "Message", "rows": 5}))
    forcefield = forms.CharField(required = False, widget = forms.HiddenInput, label = "leave empty", validators = [should_be_empty])