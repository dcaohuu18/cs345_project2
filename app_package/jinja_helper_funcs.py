import math
from datetime import datetime
from urllib.parse import urlsplit, urlunsplit


def reformat_datetime(datetime_obj, input_format='%Y-%m-%d %H:%M:%S', output_format='%H:%M %m/%d/%y'):
    return datetime.strptime(str(datetime_obj), input_format).strftime(output_format)


def base_url(full_url):
    split_url = urlsplit(full_url)
    return f"{split_url.scheme}://{split_url.netloc}"


def est_read_time(chars_num, chars_per_min=1000):
    return math.ceil(chars_num/1000) # round up