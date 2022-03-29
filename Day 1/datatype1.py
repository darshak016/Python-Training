"""Saurabh needs to withdraw X Rs. from an ATM. The transaction will succeed only if X is an odd number, 
and Saurabh's account balance has enough cash to perform the withdrawal transaction (including bank charges). 
For each successful withdrawal the bank charges 10.50 Rs. Calculate Saurabh's account balance after an attempted transaction.

Input:
- Saurabh's initial account balance
- Withdrawal amount

Output
- Amount present in Saurabh's account after withdrawal.
- Error message, if the withdrawal did not match transaction criteria.
"""

balance = float(input("Enter initial amount : "))
withdrawal_amount = float(input("Enter Withdrawal amount : "))
charge = 10.50
if withdrawal_amount<balance:
    if withdrawal_amount % 2 != 0:
        balance = balance - withdrawal_amount - charge
        print(balance)
    else:
        print("Transection must be odd")
else:
    print("Insufficient Balace") 
           