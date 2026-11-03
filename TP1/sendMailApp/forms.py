from django import forms


class contactForm(forms.Form):
    from_email = forms.EmailField()
    subject = forms.CharField()
    mesage = forms.CharField(widget = forms.Textarea)
    to_email = forms.EmailField()
    