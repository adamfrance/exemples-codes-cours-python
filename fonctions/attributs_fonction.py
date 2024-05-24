def multiplication(a, b=3):
    """Retourne a multiplié par b
    :param a: telle valeur
    :param b: connection untel
    """
    return a * b

if __name__ == "__main__":
    special_attributes = [
        "__doc__", "__name__", "__qualname__", "__module__",
        "__defaults__", "__code__", "__globals__", "__dict__",
        "__closure__", "__annotations__", "__kwdefaults__",
    ]
    for attribut in special_attributes:
        print(attribut, '==>', getattr(multiplication, attribut))