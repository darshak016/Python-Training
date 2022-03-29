"""Write a program that takes the input from the user (i.e., N). 
Create the generator function that takes this input as an argument and returns numbers from 1 to N. 

Output:
- Using the generator function, print the numbers from 1 to N.
"""

number = int(input("Enter Integer Number : "))

def generate_integer(number):
    for i in range(1,number+1):
        yield i

for i in generate_integer(number):
    print(i)