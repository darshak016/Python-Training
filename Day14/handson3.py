"""Calculate time taken by function in the function execution using decorator.
    For example:
    >>> waste_some_time(1)
    Finished 'waste_some_time' in 0.0010 secs

    >>> waste_some_time(999)
    Finished 'waste_some_time' in 0.3260 secs
"""
import time

def waste_some_time_decorator(fun):
    def wrapper(*args,**kwargs):
        starttime = time.time()
        fun(*args,**kwargs)
        endtime = time.time()
        return "Finished {} in {} secs".format(fun.__name__,endtime-starttime)        
    
    return wrapper

@waste_some_time_decorator
def waste_some_time(number):
    for _ in range(100*number):
        continue


def main():
    take_time = waste_some_time(1000)
    print(take_time)

if __name__ == "__main__":
    main()