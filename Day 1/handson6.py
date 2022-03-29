"""Write a python function which counts the frequency of given character in a given string.
Inputs - A String A Character whose frequency needs to be determined
"""

test_string = str(input("Enter String : "))

freq = {}

for i in test_string:
    if i in freq:
        freq[i] += 1
    else:
        freq[i] = 1    
        