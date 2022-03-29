"""Write a program to take size of the list as input. 
Then read the integer values and store these details into list. 

Output:
- The list entered by the user.
"""

print("Enter Integer List : ")
_list = list(map(int, input().split()))
print(_list)