import logging

def function_logger(func):
	logging.basicConfig(level = logging.INFO, filename="main.log")
	
	def decorated_func(*args, **kwargs):
		log_str = f'calling {func.__name__}'
		
		if args:
			log_str += f' with arguments {args}'
		if kwargs:
			log_str += f', {kwargs}'
		
		result = func(*args, **kwargs)
		print(log_str + f", return value: {result}")
		
		return result

	return decorated_func