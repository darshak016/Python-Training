"""Write a Python program to get a string made of the first 2 
and the last 2 chars from a given a string. 
If the string length is less than 2, return "Empty String"
"""

str = input("Enter String : ")

if len(str) < 2:
    print("Empty String")
    
else:
    new_string = str[0:2] + str[-2:]
    print(new_string)    
