"""Write a program check_inputs.py that gets two inputs and checks that the first represents a valid int 
number and that the second represents a valid float number.
"""

def main():
    input1 = input("Enter input1: ")
    input2 = input("Enter input2: ")
    
    try:
        int_input = int(input1)
        
    except ValueError:
        print("{} is not a valid first input, expected a int value.".format(input1))     
    

    try:
        float_input = float(input2)
        
    except ValueError:
        print("{} is not a valid first input, expected a int value.".format(input2))
        
        
if __name__ == '__main__':
    main()