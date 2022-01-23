import types

"""
when there is a need to dynamically changing the behavior
of an object, we offer the abstract strategy class
when there is a need, we provide another variation of that class
we will use "types" module, that supports the dynamic creation of new types
"""


class Strategy:

    def __init__(self, function=None):
        self.name = "Default strategy"
        if function:
            self.execute = types.MethodType(function, self)

    def execute(self):
        """this is the default method that we can replace"""
        print("{} is used!".format(self.name))


def strategy_one(self):
    print("{} is used to execute method 1".format(self.name))


def strategy_two(self):
    print("{} is used to execute method 2".format(self.name))


s0 = Strategy()
s0.execute()

s1 = Strategy(strategy_one)
s1.name = "Strategy one"
s1.execute()

s2 = Strategy(strategy_two)
s2.name = "Strategy two"

s2.execute()
