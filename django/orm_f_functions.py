# DON'T
for person in Person.objects.all():
    person.age += 1
    person.save()
# DO
Person.objects.update(age=F('age') + 1)