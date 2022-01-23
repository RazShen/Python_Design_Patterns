from functools import wraps
"""
allow users to add new features to objects without changing their
structure dynamically without using subclass
"""

def make_blink(function):
    """
    defines the decorator
    """
    @wraps(function)

    def decorator():
        """
        grab the return value of the decorated function
        """
        ret = function()
        """
        add new functionality to the decorated function
        """
        return "<blink>" + ret + "</blink>"

    return decorator

@make_blink
def hello_world():
    """ original function"""
    return "Hello, World"

print(hello_world())
print(hello_world.__name__)