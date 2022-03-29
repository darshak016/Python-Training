"""Write a Python program to convert a date of yyyy-mm-dd format to dd-mm-yyyy format
"""
import re

def convert_date(input_date):
    """function to convert format of date

    Args:
        input_date ([string]): give date in [yyyy-mm-dd] format

    Returns:
        [string]: return date in [dd-mm-yyyy] format
    """
    pattern = r'(\d{4})-(\d{1,2})-(\d{1,2})'
    replace =  '\\3-\\2-\\1'
    
    date = re.sub(pattern,replace, input_date)
    return date
       
    
  