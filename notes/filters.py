from .models import Note
import django_filters

class ListFilter(django_filters.FilterSet):
    class Meta:
        model = Note
        fields = [
            'year',
            'semester',
            'branch',
        ]
