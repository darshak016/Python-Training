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
from mapquest import Mapquest

def main():
    try:
        key = input("Enter API key: ")
        client = Mapquest(key)    
    except Exception as e:
        print(e)
        
    else:
        print("........get_address.......")
        response = client.address_get("Denver,CO")
        print(response) 
        
        print("........post_address.......")
        response = client.address_post("Washington,DC")
        print(response) 
        
        print("........get_reverse.......")
        response = client.get_reverse(38.892062, -77.01991)
        print(response) 
        
        print("........post_reverse.......")
        response = client.post_reverse(21.186461, 72.808128)
        print(response) 
        
        print("........get_batch.......")
        response = client.post_batch(["Washington,DC","Surat, INDIA"])
        print(response)
        
        print("........post_batch.......")
        response = client.post_batch(["Washington,DC","Surat, INDIA"])
        print(response)    

if __name__ == "__main__":
    main()