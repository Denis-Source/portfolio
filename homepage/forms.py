from django import forms


class ContactForm(forms.Form):
    class Meta:
        fields = ["name", "email", "subject", "message"]

    name = forms.CharField(widget=forms.TextInput(
        attrs={
            "class": "form-control"
        }
    ))
    email = forms.CharField(widget=forms.EmailInput(
        attrs={
            "class": "form-control"
        }
    ))
    subject = forms.CharField(widget=forms.TextInput(
        attrs={
            "class": "form-control"
        }
    ))
    message = forms.CharField(widget=forms.Textarea(
        attrs={
            "class": "form-control"
        }
    ))
