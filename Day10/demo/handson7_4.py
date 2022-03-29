"""Write a python program to check valid IPV4 and IPV6 ip address 
"""

import re
    
def check_ipv4(string):
    """check wether given ipv4 is valid or not

    Args:
        string ([string]):

    Returns:
        [bol]: return boolean based on given ipv4
    """
    ipv4 = string
    pattern_ipv4 = "^((25[0-5]|(2[0-4]|1[0-9]|[1-9]|)[0-9])(\\.(?!$)|$)){4}$"
    
    result = re.match(pattern_ipv4, ipv4)
    if result:
        return True
    else:
        return False   
        
def check_ipv6(string):
    """check wether given ipv4 is valid or not

    Args:
        string ([string]): 

    Returns:
        [bol]: return boolean based on given ipv6
    """
    ipv6 = string
    pattern_ipv6 = r"([A-F0-9]{1,4}:){7}[A-F0-9]{1,4}"   
    
    result = re.match(pattern_ipv6, ipv6)
    if result:
        return True
    else:
        return False       
        
      