"""
Helps untangle unnecessarily complicated class hierarchy

Bridge is a structural design pattern that lets you
split a large class or a set of closely related classes
into two separate hierarchies—abstraction and implementation—which
can be developed independently of each other.


"""

class DrawAPI1:
    def draw(self, radius, color):
        return "API 1 radius {} color {}".format(radius,color)

class DrawAPI2:
    def draw(self, radius, color):
        return "API 2 radius {} color {}".format(radius,color)

class Circle():
    """here we send draw_api as a pointer to class,
    instead of creating 2 different circles with each
    built in draw_api, we need only 1 class circle"""
    def __init__(self,radius,color, draw_api):
        self._radius = radius
        self._color = color
        self._draw_api = draw_api

    def draw(self):
        return self._draw_api.draw(self._radius, self._color)


circle1 = Circle(1,"Blue", DrawAPI1())
circle2 = Circle(2,"Red", DrawAPI2())

print(circle1.draw())
print(circle2.draw())


