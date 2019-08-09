from django import forms


class ContactForm(forms.Form):
    email = forms.EmailField(widget=forms.TextInput(attrs={'class' : 'w3-input w3-border', 'placeholder' : 'Email'}), required=True)
    mailer = forms.BooleanField(widget=forms.CheckboxInput(attrs={'class' : 'w3-check'}))