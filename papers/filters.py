from .models import Paper
import django_filters
from stubit1.choices import *

class ListFilter(django_filters.FilterSet):
    class Meta:
        model = Paper
        fields = [
            'year',
            'semester',
            'branch',
        ]
