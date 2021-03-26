# DON'T
count = len(Person.objects.all())  # Evaluates the entire queryset
# DO
count = Person.objects.count()  # Executes more efficient SQL to determine count



# DON'T
exists = len(Person.objects.all()) > 0
# DO
exists = Person.objects.exists()