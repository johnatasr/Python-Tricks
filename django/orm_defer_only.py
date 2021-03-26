"Use these in favor of values() when you need a QuerySet instead of a list of dicts."


queryset = Person.objects.defer('age')  # Imagine age is computationally expensive
for person in queryset:
    print(person.id)
    print(person.name)


queryset = Person.objects.only('name')
for person in queryset:
    print(person.name)