"""Create a decorator which makes a class singleton.
    In software engineering, the singleton pattern is a software design pattern that restricts the instantiation of a class to one "single" instance. This is useful when exactly one object is needed to coordinate actions across the system.
    Reference: https://en.wikipedia.org/wiki/Singleton_pattern
    
    When used on class It should show similar output as “TheOne” class as follows:
    
    >>> first_one = TheOne()
    >>> another_one = TheOne()
    
    >>> id(first_one)
    140094218762280

    >>> id(another_one)
    140094218762280
    
    >>> first_one is another_one
    True
"""

def singleton(cls):
    """Return either existing instance of class or create new instance

    Returns:
        _class_ 
    """
    instance = [None]
    def wrapper(*args,**kwargs):
        if instance[0] is None:
            instance[0] = cls(*args,**kwargs)
        return instance[0]
    return wrapper    
    
@singleton
class TheOne:
    """Singleton class
    """
    _instance = 2
    def __init__(self):
        print("Initialize")
        
def main():
    first_one = TheOne()
    print(id(first_one))
    
    another_one = TheOne()
    print(id(another_one))           
            
if __name__ == "__main__":
    main()     