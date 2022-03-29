"""Write a program to take two integers  as input. Print those two 
integers as output and then call a function to swap those two integers.
	- Write function for each possible way to swap two integers 
"""

 
num1, num2 = map(int, input("Enter two integer : ").split())

def swap_using_variable(num1,num2):
    num1,num2 = num2,num1
    print("number1 : ",num1, "number2 : ",num2)
    
def swap_using_third_variable(num1,num2):
    temp = num1
    num1 = num2
    num2 = temp
    print("number1 : ",num1, "number2 : ",num2)    
    
def swap_using_xor(num1,num2):
    num1 = num1 ^ num2
    num2 = num1 ^ num2
    num1 = num1 ^ num2
    print("number1 : ",num1, "number2 : ",num2)
    
def swap_using_arith_operator(num1,num2):
      num1 = num1 + num2
      num2 = num1 - num2
      num1 = num1 - num2
      print("number1 : ",num1, "number2 : ",num2)
      
def swap_using_multiplication_operator(num1,num2):
      num1 = num1 * num2
      num2 = num1 / num2
      num1 = num1 / num2
      print("number1 : ",int(num1), "number2 : ",int(num2))
  
print("Swap using direct variable : ")            
swap_using_variable(num1, num2)
print("Swap using third variable")
swap_using_third_variable(num1, num2)
print("Swap using Xor")   
swap_using_xor(num1, num2)
print("Swap using Arithmetic operator")
swap_using_arith_operator(num1, num2)
print("Swap using Multiplication operator")
swap_using_multiplication_operator(num1, num2) 