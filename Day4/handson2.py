"""Write a program that takes a number from user. If negative number is provided then raises an exception. 
"""

def main():
    
    try:
        number = int(input("Enter number: "))
        if number < 0:
            raise Exception("That is a negative number! ")
    except Exception as e:
        print(e.args[0])

if __name__ == '__main__':
    main()