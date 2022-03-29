"""Write python script to take no of arguments as input from the user.
Then read the arguments from the standard input.
Print read arguments  on output
"""


argument_list = []
argument_no = int(input("Enter Number Of Argument : "))

for i in range(argument_no):
    argument_list.append(input("Argument No" + str(i + 1) + " : "))
for i in range(argument_no):
    print(argument_list[i])    

