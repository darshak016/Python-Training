"""Write a program to input 2 strings, and merge the reversed strings separated with $.
Sample strings : abcd wxyz
Output string: dcba$zyxw
"""

str1 = input("Enter first string: ")
str2 = input("Enter second string: ")

result = str1[::-1] + "$" + str2[::-1]
print(result)