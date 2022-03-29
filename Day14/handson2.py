"""Log function arguments and return values using the decorator.
For example:
>>> make_greeting("Benjamin")
Calling make_greeting('Benjamin')
'make_greeting' returned 'Howdy Benjamin!'
'Howdy Benjamin!'

>>> make_greeting("Richard", age=112)
Calling make_greeting('Richard', age=112)
'make_greeting' returned 'Whoa Richard! 112 already, you are growing up!'
'Whoa Richard! 112 already, you are growing up!'

>>> make_greeting(name="Dorrisile", age=116)
Calling make_greeting(name='Dorrisile', age=116)
'make_greeting' returned 'Whoa Dorrisile! 116 already, you are growing up!'
'Whoa Dorrisile! 116 already, you are growing up!'
"""
from functools import wraps

def log(function):
    @wraps(function)
    def wrapper(*args,**kwargs):
        args_repr = [repr(n) for n in args]
        
        kwargs_repr = ["{}={}".format(key,value) for key,value in kwargs.items()]
        
        signature = ", ".join(args_repr + kwargs_repr)
        
        print("Calling {}({})".format(function.__name__,signature))
        
        make_greeting_str = function(*args,**kwargs)
        print("{} returned \'{}\'".format(function.__name__,make_greeting_str))
        return make_greeting_str
    
    return wrapper

@log
def make_greeting(name:str,age:int = None):
    if age == None:
        return "\'Howdy {}!\'".format(name)
    else:
        return "\'Whoa {}! {} already, you are growing up!\'".format(name,age)  

def main():
    s1 = make_greeting("Benjamin")
    print(s1)
    
    s2 = make_greeting(name="Richard", age=116)
    print(s2)
    
    s3 = make_greeting("Dorrisile", age=112)
    print(s3)

if __name__ == "__main__":
    main()