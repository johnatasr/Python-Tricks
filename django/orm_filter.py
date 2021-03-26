# DON'T
for person in Person.objects.all():
    if person.age >= 18:
        # Do something
# DO
for person in Person.objects.filter(age__gte=18):
    # Do something