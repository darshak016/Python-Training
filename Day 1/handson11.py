"""Write a program a function for ATM machine which takes amount as input and output 
should be number of notes of each denomination. The ATM has notes in following denomination : 2000, 500, 100.  
Note that the ATM machine rarely gives all notes of a single amount. 
If you enter 4000, it will give 1 2000rs, 3 500rs and 5 100rs notes for even distribution. 
"""

amount = int(input("Enter Amount : "))
note_2000=note_500=note_100 =0
if amount>2000:
    note_2000 = int(amount/2000)
    note_2000 -= 1 if note_2000!=1 else 0
    amount -= note_2000*2000
    
if amount>500:
    note_500 = int(amount/500)
    note_500 -= 1 if note_500!=1 else 0
    amount -= note_500*500

if amount>100:
    note_100 = amount//100
    amount -= note_100*100
    
print("Note Distribution is :")
print("2000Rs : ",note_2000,"\n500Rs : ",note_500, "\n100Rs : ",note_100)    
    