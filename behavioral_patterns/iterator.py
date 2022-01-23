"""
Allowing a client to access sequential elements of an aggregated object
without exposing its underlying structure
"""

def count_to(count):
    numbers_in_german = ["eins", "zwei", "drei", "vier", "funf"]

    iterator = zip(range(count),numbers_in_german)
    for position, number in iterator:
        yield number


for num in count_to(3):
    print("{}".format(num))