from django import forms
from .models import Docs


class DocsForm(forms.ModelForm):
    class Meta:
        model = Docs
        fields = ('title', 'author', 'pdf')
