import datetime

def logger(func):
	def new_func(*args, **kwargs):
		func_call_datetime = datetime.datetime.now()
		filename = 'locallogger'
		print('log file name: ', filename)
		func_data = func(*args, ** kwargs)
		return func_data
		with open (f'{filename}.log', 'a') as file:
			file.write(f'We call for {func.__name__} at time {func_call_datetime}\n')
			file.write(f'Args was {func_data}\n')
	return new_func

def logger_askfile(func):
	def new_func(*args, **kwargs):
		#filename = input('Input log file name')
		filename = 'locallogger1'
		func_call_datetime = datetime.datetime.now()
		print('log file name: ', filename)
		func_data = func(*args, ** kwargs)
		return func_data
		with open (f'{filename}.log', 'a') as file:
			file.write(f'We call for {func.__name__} at time {func_call_datetime}\n')
			file.write(f'Args was {func_data}\n')
	return new_func