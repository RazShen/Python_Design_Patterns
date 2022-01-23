"""
A subject and multiple observers
A subject should be monitored, and observer should be notified

"""

class Subject(object):
    """what is being observed"""

    def __init__(self):
        self._observers = []

    def attach(self, observer):
        if observer not in self._observers:
            try:
                self._observers.append(observer)
            except ValueError:
                pass

    def detach(self, observer):
        try:
            self._observers.remove(observer)
        except ValueError:
            pass

    def notify(self, modified=None):
        for observer in self._observers:
            if modified != observer:
                observer.update(self)

class Core(Subject):
    def __init__(self, name =""):
        Subject.__init__(self)
        self._name = name
        self._temp = 0 #if the temperature changes, we want to notify the observers

    @property
    def temp(self):
        return self._temp

    @temp.setter
    def temp(self,temp):
        self._temp = temp
        self.notify()

class TempViewer:
    def update(self, subject):
        print("Temp viewer {} has temperature {}".format(subject._name, subject._temp))



c1 = Core("core 1")
c2 = Core("core 2")

v1 = TempViewer()
v2 = TempViewer()

c1.attach(v1)
c1.attach(v2)

c1.temp = 80
c1.temp = 90
