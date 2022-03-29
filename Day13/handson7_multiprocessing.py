"""Add following features in above example.
a.      Create different processes for API call and File writing.
b.      Manage communication between processes.
	(Hint: Use queue for inter-process communication)
"""

import requests
import logging
import threading
import json
import os
from queue import Queue
import concurrent.futures

logging.basicConfig(filename="log.log", filemode="w", level=logging.DEBUG,
                    format="%(asctime)s %(levelname)s : %(message)s")

lat_lon_data = [[30.333472, -81.470448],
                [39.247478, -106.300194],
                [38.547871, -106.938622],
                [40.255306, -103.803062],
                [30.193626, -85.683029],
                ]
output_list = []

def api_call(lat_long):
    """This function call api from mapquest and response is stored in the output_list

    Args:
        lat_long (_list_): latitide and longitude taken from lat_lon_data list
    """
    logging.info("process  {} is running".format(os.getpid()))
    url = "https://www.mapquestapi.com/geocoding/v1/reverse"
    key = "dTnNUsIGLsnAKxfMAGulGSLpvGZ4eGsC"
    parameter = {"key": key, "location": str(lat_long[0]) + "," + str(lat_long[1])}
    try:
        logging.info("Thread [{}] API call".format(
            threading.current_thread().name))
        res = requests.get(url, params=parameter)
    except Exception as e:
        logging.error("Error occurred during API call")
    else:
        try:
            logging.info(" Thread [{}] Response received".format(
                threading.current_thread().name))
            res = json.loads(res.text)
            if res["info"]["statuscode"] == 0:
                res = res["results"][0]["locations"][0]
                # store json data into dictionary
                address = {
                    "street": res["street"],
                    "neighborhood": res["adminArea6"],
                    "city": res["adminArea5"],
                    "county": res["adminArea4"],
                    "state": res["adminArea3"],
                    "country": res["adminArea1"],
                    "postal_code": res["postalCode"],
                }
                print(address)
        except Exception as e:
            logging.error("Thread [{}] ".format(e))
    return address        

def write_file(address):
    """from output_list write json data into file 

    Args:
        address (_dict_):
    """
    street_name = address["street"]
    if street_name == "":
        street_name = "street"
    else:    
        street_name = street_name.replace(" ", "_")
        file_name = street_name + "_" + address["postal_code"] + ".json"
        data_json = json.dumps(address)

        try:
            with open(file_name, "w") as file:
                file.write(data_json)
                logging.info("Thread [{}] JSON data is stored in file".format(
                            threading.current_thread().name))
        except Exception as e:
            logging.error("Thread [{}] e".format(e))

def main():
    try:
        no_thread_to_call_api = int(input("Enter number of thread to call api: "))
        no_thread_to_write_file = int(input("Enter number of thread to write file: "))
        q = Queue()
        #Processpool to call api_call function
        with concurrent.futures.ProcessPoolExecutor(no_thread_to_call_api) as e:
            q.put(e.map(api_call,lat_lon_data))
        #Processpool to call write_file function
            with concurrent.futures.ProcessPoolExecutor(no_thread_to_write_file) as e:
                e.map(write_file,q.get())  
     
    except Exception as e:
        logging.error(e)
    
        
if __name__ == "__main__":
    main()