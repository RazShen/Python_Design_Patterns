"""
Creational design pattern:
Factory design pattern purpose is hiding the creation
logic from the client and return newly created
object using a common interface

If we didn't use factory here- the client should have created
a dog or cat a cat by its own, so factory eases the
use of creating a new object
"""


class Dog:

    def __init__(self, name):
        self._name = name

    def speak(self):
        return "Woof!"


class Cat:

    def __init__(self, name):
        self._name = name

    def speak(self):
        return "Meow!"


def get_pet(pet="dog"):
    """The factory method"""
    pets = dict(dog=Dog("Hope"), cat=Cat("Peace"))
    return pets[pet]


d = get_pet("dog")
print(d.speak())

c = get_pet("cat")
print(c.speak())
