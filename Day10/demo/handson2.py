"""Create a class `Account` with an int attribute `balance` and two methods add, and subtract which only take a 
single positive integer as an argument and respectively adds or subtracts them from the balance or raises ValueError 
if the balance is not sufficient. Write unit tests to test all the methods with 100% coverage.
"""

class Account:
    def __init__(self,balance):
        self.balance = balance
    
    def add(self,amount:int):
        """add amount in the account

        Args:
            amount (int): amount to be added in the account

        Returns:
            [int]: return available balance
        """
        if amount < 0:
            raise ValueError("Enter positive integer")
        self.balance += amount
        return self.balance    
           
    def subtract(self,amount:int):
        """withdraw amount from account

        Args:
            amount (int): amount to be withdraw from account

        Raises:
            ValueError: raise if balance in not enough in accont

        Returns:
            [type]: return available balance
        """
        if amount < 0:
            raise ValueError("Enter positive integer")
        elif self.balance < amount:
            raise ValueError("Insufficient balance")                 
        else:
            self.balance -= amount
            return self.balance
        