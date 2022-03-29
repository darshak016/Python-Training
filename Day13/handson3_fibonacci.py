"""Implement basic function for finding n'th fibonacci number of series. (function must sleep for 0.001second after each iteration)
a) Take list of N numbers and find respective fibonacci number without using multiprocessing and show after results of all numbers are ready.
b) Take list of N numbers and find their respective fibonacci number using multiprocessing and show after results of all numbers are ready.
c) Analyse time taken, cpu usage, memory usage
"""

import time
import multiprocessing
import os
import tracemalloc
import psutil

def fibonacci(n):
    time.sleep(0.2)
    if n == 1:
        return 1
    if n == 2:
        return 1
    else:
        return fibonacci(n-1) + fibonacci(n-2)

def main():
    starttime = time.time()
    _list_number = [3,4,5,6,7,8,8]
    
    #memory usage
    tracemalloc.start()
    
    #find fibonacci without using multiprocessing
    result = map(fibonacci,_list_number)
    print("Memory usages : {}".format(tracemalloc.get_traced_memory()[1]))
    tracemalloc.stop()
    print(list(result))
    print("function executed in {} without using multiprocessing".format(time.time()-starttime))
    #CPU usage
    print("CPU usage: {}".format(psutil.cpu_percent(1)))

    #find factorial with multiprocessing
    resettime = time.time()
    
    #memory usage
    tracemalloc.start()
    pool = multiprocessing.Pool()
    result = pool.map(fibonacci,_list_number) 
    pool.close()
    print("Memory usages : {}".format(tracemalloc.get_traced_memory()[1]))
    tracemalloc.stop()
    print(result)
    print("function executed in {} using multiprocessing".format(time.time()-resettime))
    #CPU usage
    print("CPU usage: {}".format(psutil.cpu_percent(1)))
    

  
        
if __name__ == "__main__":
    main()