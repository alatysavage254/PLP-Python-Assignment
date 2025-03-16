from typing import Self

class Car:
    def __init__(self, brand: str, horsepower: int) -> None:
        self.brand = brand
        self.horsepower = horsepower

    """ def drive(self) -> None:
        print(f'{self.brand} car is driving.')

    def get_info(self, var: int) -> None:
        print(var)
        print(f'The {self.brand} car has {self.horsepower} horsepower.') """
    
    def __str__(self) -> str:
        return f'{self.brand}, {self.horsepower}hp'
    
    def __add__(self, other: Self) -> str:
        return f'{self.brand} & {other.brand} '


volvo : Car = Car ('Volvo', 250)   
bmw : Car = Car ('bmw', 640)   
""" volvo.drive() """
""" volvo.get_info(10)  """  

print(volvo + bmw)

