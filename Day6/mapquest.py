"""Implement a demo function which will utilize the functionality.
      Using separate module instead of direct requests will avoid duplicate code for handling exceptions, 
      retry-mechanism, authentication, etc. 
      And it will be easy to update code in future at only one place instead of in each file it is used.

GeoCoding API: https://developer.mapquest.com/documentation/geocoding-api/
Getting Auth Key: https://developer.mapquest.com/user/me/apps

Only following geocoding related endpoints needs to be integrated (GET and POST).
- geocoding/v1/address
- geocoding/v1/reverse
- geocoding/v1/batch

- Use request.Session(...) to avoid repetition of authentication or header setting etc.
- Do appropriate logging in log file
- Use retry mechanism
- Use exception handling

Usage:
- import mapquest
- client = mapquest.MapQuest(...)
- response = client.get_address(...)
- response = client.post_address(...)
- response = client.get_reverse(...)


"""
# API KEY = MsFDrBOE4gDzSPHmyfh9TQUroZ3D4tTb

import requests
import json
class Mapquest:
    
    def __init__(self,key):
        """this function Initialize Mapquest object 

        """
        if self.validate_key(key):
            self.key = key
            self.user_session = requests.Session()
        
        else:
            raise Exception(".....Invalid Api key......")
            
            
    def validate_key(self,key):
        """This function check if given key is valid or not

        Args:
            key ([type]): API key

        Returns:
            [bool]: 
        """
        try:
            res = requests.get('https://www.mapquestapi.com/geocoding/v1/address?key={}'.format(key))
          
        except Exception as e:
            print(e)
            
        else:
            if res.status_code == 200:
                   return True
            else:
                return False              
            
    def address_get(self,location:str):
        """this function return longitude and latitude based on given location as parameter.

        Args:
            location (str): location to get API

        Returns:
            [str]:  return longitude and latitude
        """
        url = "https://www.mapquestapi.com/geocoding/v1/address"
        para_url = {"key": self.key, "location": location}
        
        try:
            res = self.user_session.get(url,params=para_url)
        except Exception as e:
            print(e)
        else:
            try:
                res = json.loads(res.text)
                if res["info"]["statuscode"] == 0:
                    res = res["results"][0]
                    latitude = res["locations"][0]["latLng"]["lat"]
                    longitude = res["locations"][0]["latLng"]["lng"]
                    address = "Latitude: {} and Longitude: {}".format(latitude,longitude) 
                    return address
                else:
                    return res["info"]["messages"]
                
            except KeyError as e:
                print(e)
            except Exception as e:
                print(e)          
                
    def address_post(self,location:str):
        """this function return longitude and latitude based on given location as parameter.
            parameter is passed in body
        Args:
            location (str): location to get API

        Returns:
            [str]:  return longitude and latitude
        """
        url = "https://www.mapquestapi.com/geocoding/v1/address?key={}".format(self.key)
        data = {"location": location}
        
        try:
            res = requests.post(url, data)
        except Exception as e:
            print(e)
        else:
            try:
                res = json.loads(res.text)
                if res["info"]["statuscode"] == 0:
                    res = res["results"][0]
                    latitude = res["locations"][0]["latLng"]["lat"]
                    longitude = res["locations"][0]["latLng"]["lng"]
                    address = "Latitude: {} and Longitude: {}".format(latitude,longitude) 
                    return address
                else:
                    return res["info"]["messages"]
                
            except KeyError as e:
                print(e)
            except Exception as e:
                print(e)                      
                
             
    def get_reverse(self,latitude:float,longitude:float):
        url = "http://www.mapquestapi.com/geocoding/v1/reverse"
        data = {"key": self.key, "location": str(latitude) + ", " + str(longitude)}
        
        try:
            res = self.user_session.get(url,params=data)
        except Exception as e:
            print(e)
            
        else:
            try:
                res = json.loads(res.text)
                if res["info"]["statuscode"] == 0:
                    res = res["results"][0]["locations"][0]
                    street = res["street"]
                    city = res["adminArea5"]
                    county = res["adminArea4"]
                    state = res["adminArea3"]
                    zipcode = res["postalCode"]    
                    address = street + " " + city + "- " + zipcode + " " + state + county
                    return address
                
                else:
                    return res["info"]["messages"]
            except KeyError as e:
                print(e)
            except Exception as e:
                print(e) 
                
                
    def post_reverse(self,latitude:float,longitude:float):
        url = "http://www.mapquestapi.com/geocoding/v1/reverse?key={}".format(self.key)
        data = {"location": str(latitude) + ", " + str(longitude)}
        
        try:
            res = requests.post(url, data=data)
            print(res.content)
        except Exception as e:
            print(e)
            
        else:
            try:
                if res["info"]["statuscode"] == 0:
                    res = res["results"][0]["locations"][0]
                    street = res["street"]
                    city = res["adminArea5"]
                    county = res["adminArea4"]
                    state = res["adminArea3"]
                    zipcode = res["postalCode"]    
                    address = street + " " + city + "- " + zipcode + " " + state + county
                    return address
                
                else:
                    return res["info"]["messages"]
            except KeyError as e:
                print(e)
            except Exception as e:
                print(e)                   
                    
                    
    def get_batch(self,location:list):
        url = "http://www.mapquestapi.com/geocoding/v1/batch"
        user_param = {"key": self.key, "location": location}
        
        try:
            res = self.user_session.get(url,params=user_param)
        except Exception as e:
            print(e)
        else:
            try:
                res = json.loads(res.text)
                if res["info"]["statuscode"] == 0:
                    res = res["results"]
                    _list = []
                    for i in range(len(res)):
                        _res = res[i]
                        latitude = _res["locations"][0]["latLng"]["lat"]
                        longitude = _res["locations"][0]["latLng"]["lng"]
                        location = _res["providedLocation"]["location"]
                        string = "Location {} with Latitude: {} and Longitude: {}".format(location,latitude,longitude)
                        _list.append(string)
                    return _list
                else:
                    return res["info"]["messages"]
                
            except KeyError as e:
                print(e)
            except Exception as e:
                print(e)     
                
                
    def post_batch(self,location:list):
        url = "http://www.mapquestapi.com/geocoding/v1/batch?key={}".format(self.key)
        user_param = {"location": location}
        
        try:
            res = requests.post(url, data=user_param)
        except Exception as e:
            print(e)
        else:
            try:
                res = json.loads(res.text)
                if res["info"]["statuscode"] == 0:
                    res = res["results"]
                    _list = []
                    for i in range(len(res)):
                        _res = res[i]
                        latitude = _res["locations"][0]["latLng"]["lat"]
                        longitude = _res["locations"][0]["latLng"]["lng"]
                        location = _res["providedLocation"]["location"]
                        string = "Location {} with Latitude: {} and Longitude: {}".format(location,latitude,longitude)
                        _list.append(string)
                    return _list
                else:
                    return res["info"]["messages"]
                
            except KeyError as e:
                print(e)
            except Exception as e:
                print(e)                           