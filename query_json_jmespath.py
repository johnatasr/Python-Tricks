import jmespath

persons: dict = {
   "persons": [
     { "name": "Johnatas", "age": 25 },
     { "name": "Gaby", "age": 23 },
     { "name": "Emilly", "age": 23 }
   ]
}

query = jmespath.search('persons[*].age', persons)
print(query)
# [25, 23, 23]

query = jmespath.search('persons[*].name', persons)
print(query)
# ['Johnatas', 'Gaby', 'Emilly']