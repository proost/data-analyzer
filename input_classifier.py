from collections import defaultdict

INPUT_CLASSIFY_MAPPER = {
    'output_range_start_datetime': 'output_period',
    'output_range_end_datetime': 'output_period',
}

def input_mapper(mangled_input_dict: dict) -> dict:
    sectioned_input_dict = dict()
    temp_list = list()
    for input_key,input_value in mangled_input_dict.items():
        if input_key in INPUT_CLASSIFY_MAPPER.keys():
            temp_list.append(mangled_input_dict[input_key])
            sectioned_input_dict[INPUT_CLASSIFY_MAPPER[input_key]] = tuple(temp_list)
        else:
            sectioned_input_dict[input_key] = input_value    
    return sectioned_input_dict




