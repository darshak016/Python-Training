"""Install future package where your script is present. Implement basic functions of Queue - putting items into queue and reading them. 
Use logging from Day 7 and log the items you write and read from queue.
Note: make sure the future package isn't installed/present in your Python core packages.
"""

import queue
import logging

def main():
    
    logging.basicConfig(filename="queue.log",level=logging.DEBUG,filemode='w',format="%(asctime)s %(levelname)s %(message)s")
    q = queue.Queue()
    logging.info("Queue is created")
    
    for i in range(5):
        q.put(i)
        logging.info("{} is inserted in queue".format(i))
    
    if not q.empty():
        val = q.get()
        logging.info("{} is popped from queue".format(val))
    else:
        logging.error("Queue is empty")    

if __name__ == "__main__":
    main()