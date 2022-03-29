# coding: utf-8
"""For the dictionary: owners = {"John": u"Dog", "Jane": b"Cat", "Jerome": u"Parrot", "Jenny": b"Dog", "Jared": u"Cow", "James": b"Dog", "Jeremy": b"Cow", "Jon": b"Parrot"}, 
write a program to swap the keys and values and store in a new dictionary “pets”. Is the resultant dictionary “pets” 
same for both Py2 and Py3? What are the changes required so that they give the same output on both Python versions.
"""

from __future__ import print_function
from future.utils import iteritems

def main():
    owners = {
        "John": u"Dog",
        "Jane": b"Cat",
        "Jerome": u"Parrot",
        "Jenny": b"Dog",
        "Jared": u"cow",
        "James": b"Dog", 
        "Jeremy": b"Cow", 
        "Jon": b"Parrot",
    }
    pets =   dict()
    
    # for key,value in owners.items(): python 3 compatible
    for key,value in iteritems(owners):
        if isinstance(value, bytes):
            pets[str(value.decode())] = key
        else:
            pets[str(value)] = key    
    print(pets)
    

if __name__ == "__main__":
    main()