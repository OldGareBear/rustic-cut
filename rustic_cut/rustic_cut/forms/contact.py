import re
from django import forms

class ContactForm(forms.Form):
    error_css_class = 'alert alert-danger'

    name = forms.CharField(
        min_length= 2,
        max_length=30,
        widget=forms.TextInput(attrs={'class':"form-control", 'id':'cname', 'placeholder':"Your Name", 'name':"name"})
    )
    email = forms.EmailField(
        max_length=500,
        widget=forms.TextInput(attrs={'class':"form-control",'id':"cemail", 'placeholder':"Your Email", 'name':"email"})
    )
    message = forms.CharField(
        max_length=600,
        widget=forms.Textarea(attrs={'class':"form-control", 'id':'cmessage', 'placeholder':"Enter Your Message", 'name':"message", 'style':"rows:12"})
    )
