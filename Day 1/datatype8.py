"""Write a program to make a new string from a given string in which the xth character should be replaced with yth character, 
where x,y and string should be taken as input from user. (x,y should be less than length of string)
Input String: Helper
x= 2
y= 4
Output: Hpleer
"""

str = input("Input String: ")
x = int(input("Enter first position of character: "))
y = int(input("Enter second position of character: "))

if x<len(str) and y<len(str):
    _list = list(str)
    temp = _list[x-1]
    _list[x-1] = _list[y-1]
    _list[y-1] = temp
    
new_str = ""   
for i in _list:
    new_str += i    
print(new_str)    
    

