import os
import datetime
from pandas import DataFrame
from celery import Celery
from analyzer.data_converter import ExcelConverter
from settings import STATICFILES_DIRS

def get_file_directory():
    static_location = ''.join(STATICFILES_DIRS)
    return static_location + '/'

APP = Celery('file_maker',backend='amqp',broker='amqp://')
FILE_DIRECTORY_PATH = get_file_directory()
FILE_LIMITAION_HOURS = 'some_int'

OUTPUT_STANDARD_MAPPER = {
    'target_result': 'target_name',
}

FILTER_STANDARD_MAPPER = {
    'filter_condition': 'condition_name',

}

@APP.task
def process_file_handling(data: 'DataFrame',file_name: str,input_dict: str):
    converted_data = ExcelConverter(input_dict).convert_to_export_excel(data)
    convert_dataframe_to_excel(converted_data,file_name,input_dict)
    delete_files_all()

def convert_dataframe_to_excel(data: 'DataFrame',file_name: str,input_dict: dict) -> str:
    file_full_path = FILE_DIRECTORY_PATH + file_name
    if input_dict['filter_standard'] == '':
        label_name = None
    else:
        label_name = FILTER_STANDARD_MAPPER[input_dict['filter_standard']]
    data.to_excel(
        file_full_path,
        index_label=label_name,
    )

def delete_files_all():
    for file_name in os.listdir(FILE_DIRECTORY_PATH):
        if '.xlsx' in file_name:
            path_to_file = FILE_DIRECTORY_PATH + file_name
            delete_file_over_limitation(path_to_file)

def delete_file_over_limitation(path_to_file: str):
    created_time = os.path.getctime(path_to_file)
    created_time = datetime.datetime.fromtimestamp(created_time).strftime('%Y-%m-%d %H:%M:%S')
    created_datetime = datetime.datetime.strptime(created_time,'%Y-%m-%d %H:%M:%S')
    if datetime.datetime.now() - created_datetime > datetime.timedelta(hours=FILE_LIMITAION_HOURS):
        os.remove(path_to_file)

def get_file_path(file_name: str) -> str:
    return FILE_DIRECTORY_PATH + file_name

