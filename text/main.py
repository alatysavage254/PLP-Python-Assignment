name: str = 'alaty'
age: int = 'eleven'

print(age)

from datetime import datetime

print(datetime.now())

def show_date() -> None:
    print('This is the date and time:')
    print(datetime.now())

show_date()
show_date()

def greet(name: str) -> None:
    print(f'Hello, {name}!')

greet('Alice')
greet('Bob')