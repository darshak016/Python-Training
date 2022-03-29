"""Write a function to find larger of three numbers. 
	- Functions for each possible way we can find larger of three numbers.
"""

number1 = int(input("Enter First Number : "))
number2 = int(input("Enter Second Number : "))
number3 = int(input("Enter Third Number : "))

def find_large_number_way1(number1, number2, number3):
    if (number1>number2) and (number1>number3):
        return number1
    elif (number2>number1) and (number2>number3):
        return number2
    else:
        return number3        
        
def find_large_number_way2(number1,number2,number3):
    return max(number1, number2, number3)

def find_large_number_way3(number1,number2,number3):       
    unsorted_list = [number1,number2,number3]
    sorted_list = unsorted_list.sort()
    return unsorted_list[-1]


print("Large number using conditional statement : ")
print(find_large_number_way1(number1, number2, number3))
print("Large number using max function : ")
print(find_large_number_way2(number1, number2, number3))
print("Large number using List : ")
print(find_large_number_way3(number1, number2, number3))