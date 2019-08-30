import pandas
from pandas import DataFrame
import string
import random

MAPPER = {
    'filter_value': 'value_name'
}

class WebConverter():
    def __init__(self,input_dict:'dict'):
        self.input_dict = input_dict
        self.result = dict()

    def convert_to_send_web(self,data:'DataFrame') -> dict:
        self.get_x_axis_labels(data)
        if self.input_dict['filter_standard'] is not None: 
            data = self.remove_sum_column(data)
        self.section_data(data)
        return self.result

    def get_x_axis_labels(self,data:'DataFrame') -> dict:
        self.result['x_axis_labels'] = list(data.index)

    def remove_sum_column(self,data:'DataFrame') -> 'DataFrame':
        for column_name in data.columns:
            if column_name == 'condition':
               data = data.drop(columns=column_name)
        return data

    def section_data(self,data: dict) -> dict:
        for column_name in data.columns:
            self.result[column_name] = list(data[column_name])

class ExcelConverter():
    def __init__(self,input_dict):
        self.input_dict = input_dict.dict() 

    def convert_to_export_excel(self,data: 'DataFrame') -> 'DataFrame':
        renamed_index_data = self.rename_index(data)
        renamed_index_name_data = self.rename_index_name(renamed_index_data)
        converted_data = self.rename_column(renamed_index_name_data,self.input_dict['filter_standard'])
        return converted_data

    def rename_index(self,data: 'DataFrame') -> 'DataFrame':
        for index_name in data.index:
            if 'condition' in index_name:
                new_index_name = self.input_dict['output_range_end_datetime'].replace('T',' ')
                data = data.rename(index={index_name:new_index_name})
        return data

    def rename_index_name(self,data: 'DataFrame') -> 'DataFrame':
        if data.index.name in NAME_MAPPER['index_name'].keys():
            data.index.name = NAME_MAPPER['index_name'][data.index.name]
        return data

    def rename_column(self,data: 'DataFrame',filter_standard: str) -> 'DataFrame':
        for column_name in data.columns:
            replaced_column_name = column_name
            if 'condition' in column_name:
                replaced_column_name = replaced_column_name.replace('condition'," condition_name ")
            for mapper_name in NAME_MAPPER['column'].keys():
                if mapper_name == filter_standard:
                    for name_in_mapper in NAME_MAPPER['column'][filter_standard].keys():
                        if name_in_mapper in replaced_column_name:
                            new_column_name = NAME_MAPPER['column'][filter_standard][name_in_mapper]
                            replaced_column_name = replaced_column_name.replace(name_in_mapper,new_column_name)
                        else:
                            continue
                elif mapper_name in column_name:
                    new_column_name = NAME_MAPPER['column'][mapper_name]
                    replaced_column_name = replaced_column_name.replace(mapper_name,new_column_name)
            data = data.rename(columns={column_name:replaced_column_name})
        return data
    
def name_file() -> str:
    name_length = 23
    string_pool = string.ascii_letters
    file_name = ""
    for _ in range(name_length):
        file_name += random.choice(string_pool)
    file_name += '.xlsx'
    return file_name


