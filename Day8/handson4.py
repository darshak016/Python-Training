"""Write a function that takes json file(demo.json) as an input, and return value for any of the requested key. (demo.json : smb://10.0.1.22/CrestData/UserData/Milan Parmar/Milan Parmar Python Training files/demo.json)
        (The key may be at any level)
        Example: If the input is “md5Hex” then output should be “377d484478843e5e2d8b7eb935cbf598”
"""
import json

def find_key(data,key):
    """This function iterate through json file to find given key

    Args:
        data ([object]): 
        key ([string]): 

    Returns:
        [string]: return value of key
    """
    if type(data) == type(dict()):
        if key in data:
            return data[key]
        for i in data:
            if type(data[i]) == type(dict()) or type(data[i]) == type([]):
                value = find_key(data[i], key)
                if value != None:
                    return value
                
    elif type(data) == type([]):
        for i in data:
            value = find_key(i, key)
            if value != None:
                return value
    return None        
            
def main():
    with open("demo.json","r") as file:
        data = json.loads(file.read())
        
        key = input("Enter key: ")
        value = find_key(data,key)
        if value:
            print("value of key {} is {}".format(key,value))   
        else:
            print("key is not found")
            
if __name__ =="__main__":
    main()
