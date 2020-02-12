from django import forms


class IndexForm(forms.Form):
    img = forms.ImageField(required = True, widget = forms.FileInput(attrs = {'class':'input'}))


