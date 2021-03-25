

people = [
    {"name": "Johantas", "age": 25},
    {"name": "Carlos", "age": 78},
    {"name": "May", "age": 15},
    {"name": "Gaby", "age": 23},
    {"name": "Lana", "age": 15},
    {"name": "Other", "age": 35},
]


sorted_people = sorted(people, key=lambda people: people['name'], reverse=True)
print(sorted_people)
