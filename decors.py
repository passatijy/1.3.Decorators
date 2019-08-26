import datetime

def logger(func):
	def new_func(*args, **kwargs):
		func_call_datetime = datetime.datetime.now()
		filename = 'logger'
		print('log file name: ', filename)
		func_data = func(*args, **kwargs)
		with open (filename + '.log', 'a') as file:
			file.write(f'{func_call_datetime} We call for {func.__name__} with args {func_data}\n')
		return func_data
	return new_func

def param_logger(filepath):
	def logger_askfile(func):
		#filename = input('Input log file name: ')
		def new_func(*args, **kwargs):
			func_call_datetime = datetime.datetime.now()
			print('log file name: ', filepath)
			func_data = func(*args, ** kwargs)
			with open (filepath + '.log', 'a') as file:
				file.write(f'{func_call_datetime} We call for {func.__name__} with args {func_data} \n')
			return func_data
		return new_func
	return logger_askfile