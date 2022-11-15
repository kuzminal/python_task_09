from os import getlogin
from psutil import virtual_memory


def fill_dict():
    keys = ['user_name', 'memory_total', 'memory_used', 'memory_percent']
    memory = virtual_memory()._asdict()
    values = [getlogin(), memory['total'], memory['used'], memory['percent']]
    return dict(zip(keys, values))
