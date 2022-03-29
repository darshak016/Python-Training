"""Create a simple class(e.g. Employee) with some attributes(e.g. name, age, gender)
and serialize-deserialize objects using JSON and Pickle and compare both of these methods. 
(Take values from user as inputs at the first time)
"""
import pickle
import json
class Employee:
    def __init__(self,name,age,gender):
        self.name = name
        self.age = age
        self.gender = gender
        
    def __iter__(self):
        return iter([("name",self.name),("age",self.age),("gender",self.gender)]) 
    
def main():
    try:
        emp_name = input("Enter employee name: ")
        emp_age = input("Enter employee age: ")
        emp_gender = input("Enter employee gender: ")
    except ValueError:
        print("Enter valid inputs")    
    else:
        obj = Employee(emp_name, emp_age, emp_gender)
        #serialize objects using Pickle
        pickled_obj = pickle.dumps(obj) 
        print("serialize-pickle {}".format(pickled_obj))
        #deserialize objects using Pickle
        unpickled_obj = pickle.loads(pickled_obj)
        print("deserialize-pickle {}".format(unpickled_obj))  
        
        #serialize objects using JSON
        json_obj = json.dumps(dict(obj)) 
        print("serialize-JSON {}".format(json_obj))
        print(type(json_obj))
        #deserialize objects using JSON
        data = json.loads(json_obj)
        print("deserialize-JSON {}".format(data))     
        print(type(data))
        
if __name__ == "__main__":
    main()    