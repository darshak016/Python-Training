"""Implement basic function for finding factorial of single number. (function must sleep or 0.001second after each iteration)
a) Take list of N numbers and find their factorial without using multithreading and show after results of all numbers are ready.
b) Take list of N numbers and find their factorial using multithreading and show after result of all number is ready.
c) Analyse time taken, cpu usage, memory usage.
"""
import time
import concurrent.futures
import tracemalloc
import psutil

def factorial(n):
    time.sleep(0.5)
    if n == 0:
        return 1
    elif n == 1:
        return 1
    else:
        return n*factorial(n-1)

def main():
    starttime = time.time()
    _list_number = [3,4,5,6,7,8,8]
    size = 7
    
    #memory usage
    tracemalloc.start()
    #find factorial without using multithreading
    result = map(factorial,_list_number)
    print("Memory usages : {}".format(tracemalloc.get_traced_memory()[1]))
    tracemalloc.stop()
    print(list(result))
    print("function executed in {} without using multithreading".format(time.time()-starttime))
    #CPU usage
    print("CPU usage: {}".format(psutil.cpu_percent(1)))
    
    #find factorial with multithreading
    resettime = time.time()
    #memory usage
    tracemalloc.start()
    with concurrent.futures.ThreadPoolExecutor(size) as executor:
        result = executor.map(factorial, _list_number)
        print("Memory usages : {}".format(tracemalloc.get_traced_memory()[1]))
        tracemalloc.stop()
        print(list(result))
        print("function executed in {} using multithreading".format(time.time()-resettime))
        #CPU usage
        print("CPU usage: {}".format(psutil.cpu_percent(1)))
        
if __name__ == "__main__":
    main()