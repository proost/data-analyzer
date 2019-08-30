import datetime
from pytz import timezone
from settings import TIME_ZONE

def mangling_input(input_dict: dict) -> dict:
    mangled_input_dict = dict()
    for input_key,input_value in input_dict.items():
        if input_key in OUTPUT_RANGE_MAPPER:
            mangled_input_dict[input_key] = OUTPUT_RANGE_MAPPER[input_key](input_value)
        elif input_value in FILTER_MANGLER_MAPPER:
            mangled_input_dict[input_key] = FILTER_MANGLER_MAPPER[input_value](input_value)
        else:
            mangled_input_dict[input_key] = input_dict[input_key]
    return mangled_input_dict

def mangling_datetime(raw_datetime: str) -> 'datetime':
    datetime_object = datetime.datetime.strptime(raw_datetime,'%Y-%m-%dT%H:%M')
    tzinfo = timezone(TIME_ZONE)
    localized_datetime_obj = tzinfo.localize(datetime_object)
    return localized_datetime_obj

def mangling_blank(_: str) -> None:
    return None

OUTPUT_RANGE_MAPPER = {
    'output_range_start_datetime': mangling_datetime,
    'output_range_end_datetime': mangling_datetime,
}

FILTER_MANGLER_MAPPER = {
    '': mangling_blank,
}

