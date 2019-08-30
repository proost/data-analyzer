from django.db.models import F
from models import TargetModel

FILTER_RELATED_TABLE_MAPPER = {
    'input': 'table_name'
}

FILTER_TABLE_FIELD_MAPPER = {
    'input': 'table_field'
}

OUTPUT_STANDARD_MAPPER = {
    'target_result': TargetModel.objects.filter('condition'),
}
