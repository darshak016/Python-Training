"""Write decorator function to implement caching mechanism in the fibonacci function 
without modifying the existing fibonacci function
"""

from functools import wraps

def fib_decorator(fun):
    """decorator function to cache fibonacci function

    Args:
        fun (_function_):

    """
    memory = {}
    @wraps(fun)
    def wrapper(*args):
        try:
            print(memory[args])
            return memory[args]
        except KeyError:
            rv = fun(*args)
            memory[args] = rv
            return rv    
    return wrapper

@fib_decorator
def fibonacci(n):
    if n < 2:
        return n
    else:
        return fibonacci(n-1) + fibonacci(n-2)
    
if __name__ == "__main__":
    fibonacci(25)