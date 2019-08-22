# people.py
from decors import logger_askfile

@logger_askfile
def get_employees(*args, **kwargs):
	print('this is a people.py')
	return args, kwargs