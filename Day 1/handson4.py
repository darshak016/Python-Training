"""Write a program to take two numbers as input parameter 
and then ask for the arithmetic parameter to be performed. 
>>> “Enter Two numbers”
10 45 
>>>“Operations to perform “ 
+ 
>>> 55 """

number1, number2 = map(int, input("Enter Two numbers").split())

selected_operator = str(input("Operations to perform : "))

if selected_operator == '+':
    print(number1+number2)
    
elif selected_operator == '-':
    print(number1-number2)
    
elif selected_operator == '/':
    print(number1/number2)
    
elif selected_operator == '*':
    print(number1*number2)            