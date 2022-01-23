"""
The adapter pattern converts the interface of a class
into another class a client is expecting
"""


class Korean:
    def __init__(self):
        self.name = "Korean"

    def speak_korean(self):
        return "An-neyoung?"


class British:
    def __init__(self):
        self.name = "British"

    def speak_english(self):
        return "Hello"

class Adapter:
    """This class changes the generic method names
    into individual method name"""

    def __init__(self, object, **adapter_method):
        """change the name of the method"""
        self._object = object
        """ this way we will use the adapter method"""
        self.__dict__.update(adapter_method)

    def __getattr__(self, attr):
        return getattr(self._object, attr)


objects = []

korean = Korean()

british = British()

objects.append(Adapter(korean, speak=korean.speak_korean))
objects.append(Adapter(british, speak=british.speak_english))

for obj in objects:
    print("{} says '{}'\n".format(obj.name, obj.speak()))



