from django import forms
from papers import models as paper_models
from links import models as link_models
from notes import models as note_models

class UploadPaper(forms.ModelForm):
    class Meta:
        model = paper_models.Paper
        fields = [
            'title',
            'branch',
            'semester',
            'subject',
            'time_period',
            'year',
            'file',
        ]

class UploadLink(forms.ModelForm):
    class Meta:
        model = link_models.Link
        fields = [
            'link_address',
            'topic_of_link',
            'branch',
            'semester',
            'subject',
            'time_period',
        ]

class UploadNote(forms.ModelForm):
    class Meta:
        model = note_models.Note
        fields = [
            'title',
            'branch',
            'semester',
            'subject',
            'time_period',
            'year',
            'file',
        ]
