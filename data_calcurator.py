import pandas
from pandas import DataFrame

def calcurate_data(
        input_dict: dict,
        mangled_data: 'DataFrame',
        columns_to_be_group_by: list
    ) -> 'DataFrame':
    for output_standard in DATA_CALCURATOR_MAPPER.keys():
        if output_standard in input_dict['output_standard']:
            result = DATA_CALCURATOR_MAPPER[output_standard](
                input_dict,
                mangled_data,
                columns_to_be_group_by
            )
            return result

def get_total_sum(
        input_dict: dict,
        mangled_data: 'DataFrame',
        columns_to_be_group_by: list
    ) -> 'DataFrame':
    calcurator = SumCalcurator(input_dict)
    list_to_concate = list()
    calcurated_by_standard_data = calcurator.calcurate_by_standards(mangled_data,columns_to_be_group_by)
    if input_dict['filter_standard'] is not None:
        unstacked_data = calcurator.unstack_filter_standard_data(calcurated_by_standard_data)
        processed_data = replace_nan_to_zero(unstacked_data) 
        sum_by_filter_standard_data = calcurator.calcurate_sum_by_filter_standard(processed_data)
        list_to_concate.append(processed_data)
        list_to_concate.append(sum_by_filter_standard_data)
    else:
        sum_by_filter_standard_data = calcurator.calcurate_sum_by_filter_standard(calcurated_by_standard_data)
        list_to_concate.append(sum_by_filter_standard_data)
    accumulated_data = calcurator.calcurate_accumulation_of_columns(list_to_concate)
    list_to_concate.append(accumulated_data)
    concated_data = calcurator.concat_result(list_to_concate)
    return concated_data

def replace_nan_to_zero(data: 'DataFrame') -> 'DataFrame':
    return data.fillna(0)
    
class SumCalcurator():
    def __init__(self,input_dict: dict):
        self.input_dict = input_dict

    def calcurate_by_standards(self,
            processed_data: 'DataFrame',
            columns_to_be_group_by: 'DataFrame'
        ) -> 'DataFrame':
        processed_data = processed_data.groupby(columns_to_be_group_by).sum()
        return processed_data

    def unstack_filter_standard_data(self,processed_data: 'DataFrame') -> 'DataFrame':
        unstacked_data = processed_data.unstack()
        droped_level_index = unstacked_data.columns.droplevel(level=0)
        unstacked_data.columns = droped_level_index
        return unstacked_data

    def calcurate_sum_by_filter_standard(self,processed_data: 'DataFrame') -> 'DataFrame':
        sum_by_filter_standard = processed_data.sum(axis=1)
        return sum_by_filter_standard.to_frame('condition')

    def calcurate_accumulation_of_columns(self,list_to_accumulation: list) -> 'DataFrame':
        concated_data = self.concat_result(list_to_accumulation)
        accumulated_data = concated_data.cumsum()
        name_map = dict()
        for old_name in accumulated_data.columns:
            name_map[old_name] = old_name + 'name'
        accumulated_data = accumulated_data.rename(name_map,axis='columns')
        return accumulated_data
    
    def concat_result(self,list_to_concat: list) -> 'DataFrame':
        concated_data = pandas.concat(list_to_concat,axis=1)
        return concated_data

DATA_CALCURATOR_MAPPER = {
    'condition': get_total_sum
}
