class PersonMeta(type):
    def __instancecheck__(cls, instance):
        return cls.__subclasscheck__(type(instance))

    def __subclasscheck__(cls, subclass):
        return (hasattr(subclass, 'name') and
                callable(subclass.name) and
                hasattr(subclass, 'age') and
                callable(subclass.age))


class PersonSuper:
    def name(self) -> str:
        pass

    def age(self) -> int:
        pass


class Person(metaclass=PersonMeta):
    pass


class Employee(PersonSuper):
    pass


class Friend:
    def name(self):
        pass

    def age(self):
        pass
    
    def outracoisa(self):
        pass


if __name__ == "__main__":

    print(issubclass(Employee, Person))
    print(issubclass(Friend, Person))