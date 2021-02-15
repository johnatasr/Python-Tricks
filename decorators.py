
def count_decorator(func: function):
    def wrapper(name, year_born, year_today):
        age: int = year_today - year_born
        return func(name, age)
    return wrapper

@count_age
def show_person(name: str, year_born: int, year_today: int = 2021):
    return f'{name} is {year_born} old'

print(show_person('Johnatas', 25))