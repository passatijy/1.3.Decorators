# salary.py
from decors import logger
@logger
def calculate_salary(*args, **kwargs):
	print('this is salary.py')
	print('Args is:', args)
	print('Kwargs is:', kwargs)
	return args, kwargs