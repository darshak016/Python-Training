"""Make a multiplier closure function which returns back a function that can be passed any number to multiply by the factor given before.
For example:
make_double = multiply(2)
make_double(5) # should print "10"
"""
def multiply(number):
    
    def multiplier(multiplier_number):
        print(multiplier_number*number)
        
    return multiplier

def main():
    m1 = multiply(2)
    m1(5)
    m2 = multiply(7)
    m2(3)

if __name__ == "__main__":
    main()