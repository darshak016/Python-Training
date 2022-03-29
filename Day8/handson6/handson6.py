"""Create a log file such as when the content of log file exceeds the 1000 line, the new log file should get 
created and the older log file should be renamed to {logfilename}0.log , {logfilename}1.log , {logfilename}2.log etc.
"""
import logging
import os
from logging.handlers import RotatingFileHandler

PATH = os.path.join(os.getcwd(),"handson6/my_log.log")

def main():
  
    log_handler = RotatingFileHandler(filename=PATH,maxBytes=500,mode="a+",backupCount=5)
    log_format = logging.Formatter("%(asctime)s %(levelname)s - %(message)s")
    log_handler.setFormatter(log_format)
    log_handler.namer = lambda x : x.replace(".log.","_") + ".log"
    _log = logging.getLogger()
    _log.addHandler(log_handler)
    _log.setLevel(logging.DEBUG)
    
    for i in range(100):
      _log.info("Line {} is created".format(i))

if __name__ == "__main__":
  main()