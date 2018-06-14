from .models import Link
import django_filters

class ListFilter(django_filters.FilterSet):
    class Meta:
        model = Link
        fields = [
            'semester',
            'topic_of_link',
            'branch',
        ]
