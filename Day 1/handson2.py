"""Write python script to take one integer argument and then print as follows:
    	- If Value >0 and Value < 10 — Small
    	- If Value > 10 and Value <100 — Medium
    	- If Value <1000 — Large
    	- If Value > 1000 — Invalid
"""

my_var = int(input("Enter Your Number : "))

if my_var > 0 and my_var < 10:
    print("Small")
    
elif my_var > 10 and my_var < 100:
    print("Medium")
    
elif my_var <= 1000:
    print("Large")
    
elif my_var > 1000:
    print("Invalid")            