"""
Allows adding new features to existing class hierarchy without changing it
the solution is to place the new behavior into a seperate class
called visitor
"""


class House(object):
    """the class being visited"""

    def __str__(self):
        return self.__class__.__name__

    def accept(self, visitor):
        visitor.visit(self)

    def work_on_hvac(self, hvac_specialist):
        print(self, "worked on by", hvac_specialist)

    def work_on_electricity(self, electrician):
        print(self, "worked on by", electrician)


class Visitor(object):
    """abstract visitor"""

    def __str__(self):
        return self.__class__.__name__


class HvacSpecialist(Visitor):
    def visit(self, house):
        house.work_on_hvac(self)


class Electrician(Visitor):
    def visit(self, house):
        house.work_on_electricity(self)


hv = HvacSpecialist()
el = Electrician()
home = House()
home.accept(hv)
home.accept(el)
