"""Write a Python function to remove the characters which have odd index values of a given string.
"""

str = input("Enter String : ")

def remove_odd(str):
    result = ""
    for i in range(len(str)):
        if i % 2 == 0:
            result = result + str[i]
    print(result)
    
print("Output String is : ")    
remove_odd(str)            

