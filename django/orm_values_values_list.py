"""
values() and values_list() provide lists, dictionaries, or tuples evaluating only the fields you specify.
"""



# DON'T
age_lookup = {
    person.name: person.age
    for person in Person.objects.all()
}
# DO
age_lookup = {
    person['name']: person['age']
    for person in Person.objects.values('name', 'age')
}




# DON'T
person_ids = [person.id for person in Person.objects.all()]
# DO
person_ids = Person.objects.values_list('id', flat=True)