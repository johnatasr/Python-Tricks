
# DON'T (contrived example)
filtered = Person.objects.filter(first_name='Shallan', last_name='Davar')
for age in range(18):
    person = filtered.get(age=age)  # Database query on each iteration
# DO (contrived example)
filtered = Person.objects.filter(  # Narrow down the QuerySet to only what you need
    first_name='Shallan',
    last_name='Davar',
    age_gte=0,
    age_lte=18,
)
lookup = {person.age: person for person in filtered}  # Evaluate the QuerySet and construct lookup
for age in range(18):
    person = lookup[age]  # No database query


# Save memory by not caching anything
for person in Person.objects.iterator():
    # Some logic