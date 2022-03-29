"""Write a program that takes two inputs from user and perform division of input1 by input2.
"""

def main():
    input1 = input("Enter Input1: ")
    input2 = input("Enter Input2: ")
    
    try:
        result = int(input1) / int(input2)
    except ZeroDivisionError:
        print("Divide by Zero exception...!!!")
    except ValueError:
        print("Invalid inputs, expected integers...!!!")
    finally:
        print("Hi, I'm from finally...!!!")        

if __name__ == '__main__':
    main()