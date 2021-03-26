# DON'T
max_age = 0
for person in Person.objects.all():
    if person.age > max_age:
        max_age = person.age
# DO
max_age = Person.objects.all().aggregate(Max('age'))['age__max']