import django_filters
from django_filters import DateFilter

from .models import *

class TestFilter(django_filters.FilterSet):
    start_date = DateFilter(field_name='date_created', lookup_expr='gte')
    end_date = DateFilter(field_name='date_created', lookup_expr='lte')
    class Meta:
        model = Test
        fields ="__all__"
        exclude = ['executor', 'date_created']