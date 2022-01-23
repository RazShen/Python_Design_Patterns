"""
Creational design pattern

Singleton is a pattern to use when we need only 1 object
to be created of a class, it is called Borg in python
Borg, unlike singleton- allows multiple object but with the same state

Singleton/borg is used when we need to keep information between multiple classes
"""


class Borg:
    _shared_data = {} # the shared data here

    def __init__(self):
        """ the __dict__ stores all the attribute which describes the object"""
        self.__dict__ = self._shared_data  # Makes _shared_data an attribute dictionary


class Singleton(Borg):  # singleton inheriting from the borg class so it uses its __dict__ also that contains _shared_data
    def __init__(self, **kwargs):
        Borg.__init__(self)
        self._shared_data.update(kwargs)

    def __str__(self):
        return str(self._shared_data) #return the attribute dictionary by printing


x = Singleton(HTTP="Hyper Text Transfer Protocol")
print(x) # we get the output of bog attribute dictionary


y = Singleton(SNMP="Simple network management protocol")
print(y) # we also updated singleton above :)
