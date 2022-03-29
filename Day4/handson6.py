"""Write a program to convert a string value to integer and raise a custom exception
"""

class CusError(Exception):
    pass
        
def main():
    try:
        try:
            user_input = input("Enter value: ")
            result = int(user_input)   
        except ValueError:
            raise CusError()         
    except CusError:
        print("Entered value can’t be converted to integer!!")   
    
    
if __name__ == '__main__':
    main()     