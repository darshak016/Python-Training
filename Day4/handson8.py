"""Write a Python program to convert a date of yyyy-mm-dd format to dd-mm-yyyy format
"""
import re

def main():
    user_input = input("Enter date in [yyyy-mm-dd] formate: ")
    pattern = r'(\d{4})-(\d{1,2})-(\d{1,2})'
    replace =  '\\3-\\2-\\1'
    
    date = re.sub(pattern,replace, user_input)
    print("Date in format [dd-mm-yyyy] is ",date)
    
if __name__ == '__main__':
    main()    