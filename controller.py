from analyzer import (
    input_mangler,
    input_classifier,
    data_taker,
    data_mangler,
    data_calcurator,
    data_converter,
)

class Controller():
    def __init__(self):
        self.input_dict = None
        self.data = None

    @classmethod
    def main(cls,input_dict: dict) -> 'DataFrame,dict':
        cl = cls()
        mangled_input_dict = cl.mangle_input(input_dict)
        cl.map_input(mangled_input_dict)
        cl.get_data_from_db()
        mangled_data,column_list_to_be_group_by = cl.mangle_data()
        result = cl.get_statistics_from_data(mangled_data,column_list_to_be_group_by)
        result_for_front = cl.convert_result_to_send_easily(result)
        return result,result_for_front

    def mangle_input(self,input_dict: dict) -> dict:
        mangled_input_dict = input_mangler.mangling_input(input_dict)
        return mangled_input_dict

    def map_input(self,mangled_input_dict: dict):
        self.input_dict = input_classifier.input_mapper(mangled_input_dict)

    def get_data_from_db(self):
        taker = data_taker.DataTaker(self.input_dict)
        self.data = taker.get_data()

    def mangle_data(self) -> 'DataFrame,list':
        mangler = data_mangler.DataMangler(self.input_dict)
        mangled_data,column_list_to_be_group_by = mangler.mangle_data(self.data)
        return mangled_data,column_list_to_be_group_by

    def get_statistics_from_data(
            self,
            mangled_data: 'DataFrame',
            column_list_to_be_group_by: list
        ) -> 'DataFrame':
        result = data_calcurator.calcurate_data(
            self.input_dict,
            mangled_data,
            column_list_to_be_group_by
        )
        return result

    def convert_result_to_send_easily(self,result: 'DataFrame') -> dict:
        converter = data_converter.WebConverter(self.input_dict)
        converted_result = converter.convert_to_send_web(result)
        return converted_result
        
    @staticmethod
    def name_file() -> str:
        file_name = data_converter.name_file()
        return file_name
