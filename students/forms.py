from django import forms
from . import models

class CreateMyNotes(forms.ModelForm):
    class Meta:
        model = models.MyNote
        fields = [
            'title',
            'body',
            'slug',
        ]
