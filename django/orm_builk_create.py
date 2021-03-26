names = ['Jeff', 'Beth', 'Tim']
creates = []
for name in names:
    creates.append(
        Person(name=name, age=0)
    )
Person.objects.bulk_create(creates)


person = Person.objects.get(id=1)
person.jobs.add(job1, job2, job3)