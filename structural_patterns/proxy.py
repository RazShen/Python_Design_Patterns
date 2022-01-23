import time

"""
postponing the object X creation due to the
high resource requierment of the object X
clients interact with the proxy  until object X
is available

in this example the object is "producer" and the proxy
is constantly checking to see when the producer is
available for a guest
"""

class Producer:
    def producer(self):
        print("Producer working")

    def meet(self):
        print("Producer has time to meet you now")

class Proxy:
    def __init__(self):
        self.occupied = "false"
        self.producer = None

    def produce(self):
        print("Proxy: proxy is checking if producer is available")

        if self.occupied == 'false':
            self.producer = Producer()
            time.sleep(2)
            self.producer.meet()
        else:
            print("Proxy: producer is busy")

p =Proxy()
p.produce()
p.occupied = "true"

p.produce()