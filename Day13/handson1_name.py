"""Implement simple function which takes name as input and returns "hello <name>" after 1 second.
Do it for N names using multithreading and multiprocessing.
"""

import threading
import time
import concurrent.futures
import multiprocessing
import os

def print_name(name):
    """Prints the hello message

    Args:
        name (_string_): 
    """
    print("[{}] Hello {}".format(os.getpid(),name))
    time.sleep(1)

def main():
    name_list = ['darshak','sujal','meet','rutvik']
    size = 4
    #Multithreading
    print("_______Multithreading_________")
    with concurrent.futures.ThreadPoolExecutor(size) as executor:
        executor.map(print_name, name_list)
    
    #Multiprocessing
    print("______Multiprocessing_______")
    pool = multiprocessing.Pool()
    pool.map(print_name,name_list) 
    pool.close()   

if __name__ == "__main__":
   main()
        