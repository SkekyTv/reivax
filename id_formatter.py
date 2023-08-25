import re

def id_str_to_int(str):
    return int(re.sub("[^0-9]", "", str))
