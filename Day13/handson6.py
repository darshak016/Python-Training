"""Add following features in above example.
a.     Take max no. of threads N for api call and M for writing into file from user.
b.     Make list of latitude and longitude and instead of passing it to function all thread must read lat. & long,
from the same global list.
c.      Make initially blank output list and all threads must write output to that list only.
d.     Threads which are writing output to file must take input from list created in C.
(Hint: Use threadpool, Use queue for inter-thread communication)
"""

import requests
import logging
import threading
import json
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
    logging.info(threading.current_thread().name + "is running")
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
            print(res)
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
                output_list.append(address)
        except Exception as e:
            logging.error("Thread [{}] ".format(e))

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
        #Threadpool to call api_call function
        with concurrent.futures.ThreadPoolExecutor(max_workers=no_thread_to_call_api) as e:
            e.map(api_call,lat_lon_data)
        #Threadpool to call write_file function
        with concurrent.futures.ThreadPoolExecutor(max_workers=no_thread_to_write_file) as e:
            e.map(write_file,output_list)       
    except Exception as e:
        print(e)
    
        
if __name__ == "__main__":
    main()