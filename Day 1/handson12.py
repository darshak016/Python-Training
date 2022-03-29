"""Read a sentence from the standard input. Find out how many times each word appear in given string. 
"""

str = list(input("Enter String : ").split())
frequency = {}

for i in str:
    if i in frequency:
        frequency[i] += 1
    else:
        frequency[i] = 1
        
for j in frequency:
    print("\n",j,frequency[i])            
        