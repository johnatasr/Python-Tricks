import abc

class Double(metaclass=abc.ABCMeta):
    """Double precision floating point number."""
    pass

Double.register(float)


issubclass(float, Double) #True

isinstance(1.2345, Double) #True