"""Write a python program to check valid IPV4 and IPV6 ip address 
"""

import re
    
def main():
    ipv4 = input("Enter IP version 4 address: ")
    pattern_ipv4 = "^((25[0-5]|(2[0-4]|1[0-9]|[1-9]|)[0-9])(\\.(?!$)|$)){4}$"
    
    result = re.match(pattern_ipv4, ipv4)
    if result:
        print("IPV4 is valid")
    else:
        print("IPV4 is not valid")   
        
    ipv6 = input("Enter IP version 6 address: ")
    pattern_ipv6 = r"^(?:[A-F0-9]{1,4}:){7}[A-F0-9]{1,4}$"    
    
    result = re.match(pattern_ipv6, ipv6)
    if result:
        print("IPV6 is valid")
    else:
        print("IPV6 is not valid")   
        
if __name__ == '__main__':
    main()        