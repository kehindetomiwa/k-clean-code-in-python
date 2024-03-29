"""Clean Code in Python - Chapter 3: General traits of good code
> Keep It Simple
"""


class ComplicatedNamespace:
    """An convoluted example of initializing an object with some properties.
    >>> cn = ComplicatedNamespace.init_with_data(
    ...    id_=42, user="root", location="127.0.0.1", extra="excluded"
    ... )
    >>> cn.id_, cn.user, cn.location
    (42, 'root', '127.0.0.1')
    >>> hasattr(cn, "extra")
    False
    """

    ACCEPTED_VALUES = ("id_", "user", "location")

    @classmethod
    def init_with_data(cls, **data):
        instance = cls()
        for key, value in data.items():
            if key in cls.ACCEPTED_VALUES:
                setattr(instance, key, value)
        return instance


cn = ComplicatedNamespace.init_with_data(
    id_=42, user="root", location="127.0.0.1", extra="excluded")
print(cn.id_, cn.user, cn.location)
#(42, 'root', '127.0.0.1')
print(hasattr(cn, "user"))
print(hasattr(cn, "extra"))


class Namespace:
    """Create an object from keyword arguments.
    >>> cn = Namespace(
    ...    id_=42, user="root", location="127.0.0.1", extra="excluded"
    ... )
    >>> cn.id_, cn.user, cn.location
    (42, 'root', '127.0.0.1')
    >>> hasattr(cn, "extra")
    False
    """
    ACCEPTED_VALUES = ("id_", "user", "location")

    def __init__(self, **data) -> None:
        accepted_data = {
            k: v for k, v in data.items() if k in self.ACCEPTED_VALUES
        }
        self.__dict__.update(accepted_data)


cn2 = Namespace(
    id_=42, user="root", location="127.0.0.1", extra="excluded")
print(cn2.id_, cn2.user, cn2.location)
#(42, 'root', '127.0.0.1')
print(hasattr(cn2, "user"))
print(hasattr(cn2, "extra"))
