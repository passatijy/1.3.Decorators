# main.py
from application.salary import calculate_salary
from application.db.people import get_employees
print('this is a main.py')

print('__name__ = :', __name__)

if __name__ == '__main__':
	get_employees()
	calculate_salary()