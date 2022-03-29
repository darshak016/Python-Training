"""Create a json file in following format.    {
""folder_name_1"": [filename_1, filename_2, ....],
""folder_name_2"": [filename_1, filename_2, ....
        .
        .
        .
    }
Fetch folder names from the json file and if that folder is present in a predefined location using pythonic way 
then check if all the files mentioned in the list is present or not.

   Print all the files as INFO level log which are present in the folder.
   Print all the files as CRITICAL level log which are not present in the folders in log files.
"""

from os.path import exists
import json
import logging

def main():
    try:
        key_user = input("Enter key or folder name: ")
        
        #Read json file
        with open("./handson2/handson2.json","r") as file:
            data = json.load(file) 
    
        #iterate each value of key
        for i in data[key_user]:
            file_exists = exists("handson2\{}\{}".format(key_user,i))
            if file_exists == True:
                logging.info("File {} is present in {} folder".format(i,key_user))         
            else:
                logging.critical("File {} is not present in {} folder".format(i,key_user))
    except Exception as e:
        print(e)    


if __name__ == '__main__':
    main()
    
    
    
    