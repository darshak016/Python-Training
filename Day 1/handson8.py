"""Write a Python program to add 'ing' at the end of a given string 
(length should be at least 3). 
If the given string already ends with 'ing' then add 'ly' instead. 
If the string length of the given string is less than 3, leave it unchanged.
"""

str  = input("Enter String : ")

if len(str) < 3:
    print(str)
elif str[-3:] == "ing":
    str = str + "ly"
    print(str)
else:
    str = str + "ing"
    print(str)    
