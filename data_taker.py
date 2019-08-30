from analyzer.db_model_config import (
    OUTPUT_STANDARD_MAPPER,
    FILTER_RELATED_TABLE_MAPPER,
    FILTER_TABLE_FIELD_MAPPER,
)

class DataTaker():
    def __init__(self,input_dict: dict):
        self.input_dict = input_dict

    def get_data(self) -> list:
        queryset = self.set_queryset()
        queryset = self.choose_data_values(queryset)
        queryset_result = self.query_to_db(queryset)
        return queryset_result

    def set_queryset(self) -> 'queryset':
        queryset = self.mount_output_standard()
        queryset = self.mount_output_datetime_range(queryset)
        if self.input_dict['filter_standard'] is not None:
            queryset = self.mount_filter_standard(queryset)
        return queryset

    def mount_output_standard(self) -> 'queryset':
        queryset = OUTPUT_STANDARD_MAPPER[self.input_dict['output_standard']]
        return queryset        

    def mount_output_datetime_range(self,input_queryset: 'queryset') -> 'queryset':
        start_datetime,end_datetime = self.input_dict['output_period']
        queryset = input_queryset.filter(some_condition=(start_datetime,end_datetime))
        return queryset

    def mount_filter_standard(self,input_queryset: 'queryset') -> 'queryset':
        queryset = input_queryset.all().prefetch_related(
            FILTER_RELATED_TABLE_MAPPER[self.input_dict['filter_standard']]
        )
        return queryset

    def choose_data_values(self,input_queryset: 'queryset') -> 'queryset':
        value_list = list()
        value_list.append(FILTER_TABLE_FIELD_MAPPER[self.input_dict['output_standard']])
        value_list.append(FILTER_TABLE_FIELD_MAPPER["condition"])
        if self.input_dict['filter_standard'] is not None:
            value_list.append(FILTER_TABLE_FIELD_MAPPER[self.input_dict['filter_standard']])
        queryset = input_queryset.values(*value_list)
        return queryset

    def query_to_db(self,queryset:'queryset') -> list:
        queryset_result = list(queryset)
        return queryset_result
