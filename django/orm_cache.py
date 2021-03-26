"""
Use django-debug-toolbar and QuerySet.explain() to help determine the bottlenecks in your code.

"""

queryset = Person.objects.all()
list(queryset)  # Queryset evaluated and cached
print(queryset[0])  # Cache used


# DO
queryset = Person.objects.all().select_related('father')  # Foreign key object is included in query and cached
for person in queryset:
    person.father  # Hits the cache instead of the database

queryset = Person.objects.all().prefetch_related('children') # Foreign key object is included in query and cached
for person in queryset:
    person.children  # Hits the cache instead of the database