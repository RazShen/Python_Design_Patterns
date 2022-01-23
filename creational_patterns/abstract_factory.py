"""
Creational design pattern:

abstract factory is useful when the user expects to
receive a family of related object at a given time,
but doesn't have to know until runtime

An abstract factory contains multiple factories for related items
So it will basically create factory we will need in runtime

The difference between factory and abstract factory is that factory
will generate 1 object of some type with multiple objects,
and abstract factory will be able to return 1 factory out of multiple factories
it might be useful where we want to create multiple objects out of a factory and we only
know in runtime
"""


class Dog:

    def speak(self):
        return "Woof!"

    def __str__(self):
        return "Dog"


class Cat:

    def speak(self):
        return "Mewo!"

    def __str__(self):
        return "Cat"


class DogFactory:
    """ Concrete Factory"""

    def get_pet(self):
        """returns a dog object"""
        return Dog()

    def get_food(self):
        """returns a dog food object"""
        return "Dog Food!"


class CatFactory:
    """ Concrete Factory"""

    def get_pet(self):
        """returns a cat object"""
        return Cat()

    def get_food(self):
        """returns a cat food object"""
        return "Cat Food!"


class PetStore:
    """ PetStore is housing our abstract factory
    """

    def __init__(self, pet_factory=None):
        """pet_factory is our abstract factory"""
        self._pet_factory = pet_factory

    def show_pet(self):
        """Utility method to display the details of the objects returned by the dogFactory"""
        pet = self._pet_factory.get_pet()
        pet_food = self._pet_factory.get_food()

        print("Our pet is '{}'".format(pet))


factory_cat = CatFactory()
shop = PetStore(pet_factory=factory_cat)
shop.show_pet()
