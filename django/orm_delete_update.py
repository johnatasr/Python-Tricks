# DON'T
for person in Person.objects.all():
    person.delete()
# DO
Person.objects.all().delete()



# DON'T
for person in Person.objects.all():
    person.age = 0
    person.save()
# DO
Person.objects.update(age=0)