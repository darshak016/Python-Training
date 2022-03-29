"""Write unit tests for the function created for Day-4 Hands-on with at least 2-3 different scenarios for each question.
Question no. - 6, 7, 8 & 9.

__________Question 9_______________

Write a python program to check valid IPV4 and IPV6 ip address 
"""

import pytest
from demo.handson7_4 import *

@pytest.mark.parametrize("input_ip,output_ip",[
    ("192.168.20.10",True),
    ("266.185.25.10",False),
])
def test_check_ipv4(input_ip,output_ip):
    """Test ipv4 address

    Args:
        input_ip ([string]): input ipv4
        output_ip ([bol]): based on validation of ipv4 test with given output
    """
    assert check_ipv4(input_ip) == output_ip
    
@pytest.mark.parametrize("input_ip,output_ip",[
    ("FE80:CD00:0000:0CDE:1257:0000:211E:729C",True),
    ("A5BC:C596:ACC5:J235:1452:15A4:FF52:5AB",False),
])
def test_check_ipv6(input_ip,output_ip):
    """[summary]

    Args:
        input_ip ([string]): input ipv6
        output_ip ([bol]): based on validation of ipv4 test with given output
    """
    assert check_ipv6(input_ip) == output_ip    