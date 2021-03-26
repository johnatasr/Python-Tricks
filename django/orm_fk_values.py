# DON'T
father_id = Person.objects.get(id=1).father.id  # Causes a needless database query
# DO
father_id = Person.objects.get(id=1).father_id  # The foreign key is already cached. No query