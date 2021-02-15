from dataclasses import dataclass

@dataclass
class Car:
    name: str
    color: str
    
car = Car("Gol", "Black")

print(car.name)
# 'Gol'

print(car)

# Car(name='Gol', color='Black')