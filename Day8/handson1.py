"""Create a log file using logger module. Write a function display_words() in python to read lines from a text file "story.txt" (take the file name from user), 
and display those words in INFO level log, for those words which are less than 4 characters needs to be logged as in CRITICAL level log.  
If user enter the wrong file name in input then raise ERROR in log file 
"""

import logging

def display_word():
    """this function read word from the file story.txt and generate log.

    Raises:
        Exception: exception is raise if user enters wrong file name 
        other then story.txt
    """
    file_name = input("Enter file name: ")
    if file_name == "story.txt":
        try:
            with open(file_name,"r") as file:
                read_file = file.read()
                split_word = read_file.split()
            
            for i in split_word:
                if len(i) < 4:
                    logging.critical("word {} has less then 4 character".format(i))    
                else:
                    logging.info("This in info level log")    
        except Exception as e:
            print(e)            
    else:
        raise Exception("File name is invalid")        
        
def main():
    display_word()
    
    
if __name__ == '__main__':
    main()