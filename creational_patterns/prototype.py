import copy

"""
Creational Design pattern

prototype clones objects- making a copy (and not building)

"""


class Prototype:

    def __init__(self):
        self._objects = {}

    def register_object(self, name, obj):
        self._objects[name] = obj

    def unregister_object(self, name):
        del self._objects[name]

    def clone(self, name, **attr):
        obj = copy.deepcopy(self._objects.get(name))
        obj.__dict__.update(attr)
        return obj


class Car:
    def __init__(self):
        self.name = "Suzuki"
        self.color = "Blue"
        self.wheels = "Cool wheels"

    def __str__(self):
        return '{} | {} | {}'.format(self.name, self.color, self.wheels)


c = Car()
prototype = Prototype()
prototype.register_object("car", c)
new_car = prototype.clone("car", color="Green")
print(new_car)
