# ** unpack by named keywords
def cool_function(name: str, age: int):
    print(name, age)

person_dict = { "name": 'Johnatas', "age": 25 } 
cool_function(**person_dict)
# Johnatas 25

# * unpack by position
def other_function(name: str, age: int, country: str):
    print(name, age, country)
person_list = ['Johnatas', 25, 'Brazil']
other_function(*person_list)
# Johnatas 25 Brazil