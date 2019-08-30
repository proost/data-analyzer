import pandas
from pandas import DataFrame
import datetime
from analyzer.db_model_config import FILTER_TABLE_FIELD_MAPPER
from analyzer.data_grouping_config import GROUPING_MAPPER

class DataMangler():

    def __init__(self,input_dict):
        self.input_dict = input_dict

    def mangle_data(self,data: list) -> 'DataFrame,list':
        mangled_data = self.list_to_dataframe(data)
        mangled_data = self.rename_column(mangled_data)
        mangled_data = self.unify_data_type(mangled_data)
        columns_to_be_group_by = self.group_column_if_need(mangled_data)
        column_list_to_be_group_by = self.sort_groupby_columns(columns_to_be_group_by)
        return mangled_data,column_list_to_be_group_by
    
    def list_to_dataframe(self,data: list) -> 'DataFrame':
        df = DataFrame(data)
        return df

    def rename_column(self,mangled_data: 'DataFrame') -> 'DataFrame':
        for new_name,old_name in FILTER_TABLE_FIELD_MAPPER.items():
            if old_name in mangled_data.columns:
                mangled_data.rename(columns={old_name: new_name},inplace=True)
        return mangled_data

    def unify_data_type(self,mangled_data: 'DataFrame') -> 'DataFrame':
        for column_name in mangled_data.columns:
            if not column_name in NON_UNIFY_COLUMNS:
                mangled_data = DATA_UNIFY_MAPPER[column_name](column_name,mangled_data)
        return mangled_data

    def group_column_if_need(self,mangled_data: 'DataFrame') -> dict:
        columns_to_be_group_by = dict()
        for column_name in mangled_data.columns:   
            if column_name in GROUPING_MAPPER.keys():
                if column_name == 'condition':
                    column_values = GROUPING_MAPPER[column_name](
                        mangled_data[column_name],
                        self.input_dict['output_period'],
                        self.input_dict['output_range_interval'],
                    )
                    columns_to_be_group_by[column_name] = column_values
                else:
                    column_values = GROUPING_MAPPER[column_name](mangled_data[column_name])
                    columns_to_be_group_by[column_name] = column_values
            else:
                columns_to_be_group_by[column_name] = column_name
        return columns_to_be_group_by

    def sort_groupby_columns(self,columns_to_be_group_by: dict) -> list:
        groupby_column_list = list()
        groupby_column_list.append(columns_to_be_group_by['condition'])
        if self.input_dict['filter_standard'] is not None:
            groupby_column_list.append(
                columns_to_be_group_by[self.input_dict['filter_standard']]
            )
        return groupby_column_list

def unify_string_index_to_datetime_index(
        column_name: str,
        mangled_data: 'DataFrame'
    ) -> 'DataFrame':
    mangled_data[column_name] = pandas.to_datetime(mangled_data[column_name])
    return mangled_data

def unify_data_type_to_string(column_name: str,mangled_data: 'DataFrame') -> 'DataFrame':
    mangled_data[column_name] = mangled_data[column_name].astype(str)
    return mangled_data

DATA_UNIFY_MAPPER = {
    'condition': unify_string_index_to_datetime_index,
    'condition_another': unify_data_type_to_string,
}

NON_UNIFY_COLUMNS = [
    'condition',
]