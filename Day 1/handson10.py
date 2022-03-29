"""Write a Python function to insert a string in the middle of a string. 
For odd length of string, 
remove the middle character and replace with given string.
"""

str = input("Enter String : ")
middle_str = input("Enter String that you want to insert : ")
mid_char = int(len(str)/2)
result = str[0:mid_char] + middle_str + str[-mid_char:]
print(result)