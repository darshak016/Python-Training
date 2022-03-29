"""All thread should also append their output data to output.json file using only single file object in previous example.
	(Hint: Use locking on file object)
"""

import requests
import logging
import threading
import json

logging.basicConfig(filename="log.log", filemode="w", level=logging.DEBUG,
                    format="%(asctime)s %(levelname)s : %(message)s")


def api_call(lat: float, long: float):

    logging.info(threading.current_thread().name + "is running")
    url = "https://www.mapquestapi.com/geocoding/v1/reverse"
    key = "dTnNUsIGLsnAKxfMAGulGSLpvGZ4eGsC"
    parameter = {"key": key, "location": str(lat) + "," + str(long)}

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
                street_name = address["street"]
                if street_name == "":
                    street_name = "street"
                else:    
                    street_name = street_name.replace(" ", "_")
                file_name = street_name + "_" + address["postal_code"] + ".json"
                data_json = json.dumps(address)
                #store response into json file
                try:
                    with open(file_name, "w") as file:
                        file.write(data_json)
                        logging.info("Thread [{}] JSON data is stored in file".format(
                            threading.current_thread().name))
                except Exception as e:
                    logging.error("Thread [{}] e".format(e))
                    
                #store response into output.json file
                try:
                    lock = threading.Lock()
                    lock.acquire()
                    logging.info("output.json file is locked for thread {}".format(threading.current_thread().name))
                    with open("output.json","r+") as file:
                        file_content = json.load(file)
                        file_content["root"].append(address)
                        json.dumps(file_content)
                except Exception as e:
                    logging.error(e)        
                finally:
                    logging.info("Thread [{}] is released".format(threading.current_thread().name))
                    lock.release() 
                       
        except Exception as e:
            logging.error("Thread [{}] ".format(e))


def main():
    try:
        thread_list = []
        with open("lat_long.txt", "r") as file:
            data = file.readline()
            while data:
                loc = data.split(",")
                lat, long = loc[0], loc[1]
                t = threading.Thread(target=api_call, args=(lat, long))
                t.start()
                thread_list.append(t)
                data = file.readline()
        for thread in thread_list:
            thread.join()
            logging.info(thread.name +" Completed")           
    except Exception as e:
        logging.error(e)
        
if __name__ == "__main__":
    main()