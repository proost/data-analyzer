import pandas
import datetime
from settings import TIME_ZONE

today = datetime.datetime.now()
age_range = pandas.date_range(
<<<<<<< HEAD
    start='start_year',
    end=today,
    freq='interval',
=======
    start='시작년도',
    end=today,
    freq='구간',
>>>>>>> 789cb97... data analyzer for web
    tz=TIME_ZONE,
)

def get_output_range_range(output_range:tuple,output_range_interval:str) -> 'pandas.DatetimeIndex':
    start_time,end_time = output_range
    if output_range_interval == 'time_condition':
        frequency = 'time_condition'
    output_range = pandas.date_range(
        start=start_time,
        end=end_time,
        freq=frequency,
        tz=TIME_ZONE,
    )
    return output_range

def get_output_range_label(input_output_range:tuple,output_range_interval:str) -> list:
    output_range = get_output_range_range(input_output_range,output_range_interval)
    datetime_list = list()
    for datetime_value in output_range:
        datetime_list.append(datetime_value.strftime(format='%Y-%m-%d %H:%M'))
    datetime_list.reverse()
    datetime_list.pop()
    datetime_list.reverse()
    return datetime_list

def get_output_range_group(
        key:'Series',
        output_range:tuple,
        output_range_interval:str
    ) -> 'pandas.CategoricalIndex':
    get_output_range_label(output_range,output_range_interval)
    index_group = pandas.cut(
        x=key,
        bins=get_output_range_range(output_range,output_range_interval),
        labels=get_output_range_label(output_range,output_range_interval),
    ).astype(str)
    return index_group

def get_age_label() -> list:
    age_list = list()
    for datetime_value in age_range:           
        start_year = datetime_value.year
        end_year = int(start_year) + 'some int'
        age_list.append(str(start_year) + '~' + str(end_year))
    age_list.reverse()
    age_list.pop()
    age_list.reverse()
    return age_list

def get_age_group(key:'Series') -> 'pandas.CategoricalIndex':
    index_group = pandas.cut(x=key,bins=age_range,labels=get_age_label()).astype(str)
    return index_group

GROUPING_MAPPER = {
    'condition': get_age_group,
    'condition': get_output_range_group, 
}
