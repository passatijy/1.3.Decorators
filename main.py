# main.py
from application.salary import calculate_salary
from application.db.people import get_employees
import time
print('this is a main.py')

print('__name__ = :', __name__)

if __name__ == '__main__':
	get_employees()
	calculate_salary(1,2,3,param1='a', param2='b')
	time.sleep(2)
	get_employees()
	calculate_salary(5,6,7,param1='z', param2='x')
