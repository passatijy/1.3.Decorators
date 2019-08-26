# people.py
from decors import param_logger

@param_logger('people2')
def get_employees(*args, **kwargs):
	print('this is a people.py')
	return args, kwargs