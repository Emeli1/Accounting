from datetime import datetime

from aplication.db.people import get_employees
from aplication.salary import calculate_salary


if __name__ == '__main__':
    print(datetime.today())
    calculate_salary()
    get_employees()