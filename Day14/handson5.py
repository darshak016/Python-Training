"""File locking is a mechanism that restricts access to a computer file, or to a region of a file, by allowing only one 
user or process to modify or delete it in a specific time and to prevent reading of the file while 
it's being modified or deleted. It can be used in scenarios where an API only allows one access_key 
generation. This creates race condition when multiple processes try to generate access_key and only 
one process which finishes last has the valid access_key and all other fails the subsequent calls to the API.
The problem statement is: Implement file lock using context manager.

The file lock class should allow following syntax and when ran simultaneously on two processes, it should raise error.
>>> with file_lock:
…        # do something
"""
import multiprocessing
import os
import concurrent.futures
import time

lock = multiprocessing.Lock()

class file_lock():
    """Custom context manager for file operation
    """
    is_lock = False
    def __init__(self,file_name,mode):
        self.file_name = file_name
        self.mode = mode
        
    def __enter__(self):
        if self.is_lock == False:
            self.is_lock = lock.acquire()
            print("process {} has acquired lock on file".format(os.getpid()))
            self.file = open(self.file_name,self.mode)
        return self.file
    
    def __exit__(self,exception_type,exception_class,exception_trace_route):
        if exception_type and exception_class and exception_trace_route:
            print("exception occurred in context manager")
            
        lock.release()
        print("process {} has Released lock on file".format(os.getpid()))
        self.file.close()
        print("process {} has Closed file".format(os.getpid()))
      
def file_operation(message):
    """This function execute write operation on file
    """
    with file_lock("demo.txt", "a") as file:
        file.write(message)
        time.sleep(1)
        
if __name__ == "__main__":
    process_list = ["process 1","process 2","process 3","process 4"]
    with concurrent.futures.ProcessPoolExecutor(4) as e:
        e.map(file_operation,process_list)    