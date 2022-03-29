"""Write a Python program to input a list of non-empty tuples, 
sort it in increasing order by the last element in each tuple.
Sample List : [(2, 5), (1, 2), (4, 4), (2, 3), (2, 1)]
Expected Result : [(2, 1), (1, 2), (2, 3), (4, 4), (2, 5)]
"""

_list = list(tuple(map(int, input().split()))
             for i in range(int(input("Enter number of tuples : ")))
             )

print("List Before sorting",_list)
_list.sort(key=lambda x:x[1])
print("list after sorting",_list)