"""Parse the larger CSV file (above 70 MB) and apply any aggregate function on data like Average, 
Maximum and Minimum. Make sure that memory leak should not be occurred.
"""

import csv
import gc
FILENAME = "sales_record.csv"

def read_file():
    """This function will read large csv file and store content in
        list format.
    """
    fields = []
    rows = []
    try:
        with open(FILENAME,'r') as file:
            csvreader = csv.reader(file)   
            fields = next(csvreader)
            for row in csvreader:
                rows.append(row) 
    except Exception as e:
        print(e)        
            
    max_min_avg(rows)
    print('Field names are:' + ', '.join(field for field in fields))
    
    
def max_min_avg(rows):
    """This function will calculate min, max value and average of "Total_profit"
        field

    Args:
        rows (_list_): 
    """
    total_profit = []
    for row in rows:
        total_profit.append("".join(row[:][-1:]))
    #Convert type string list to int type.    
    total_profit = [float(i) for i in total_profit]  
    
    print("Min value in Total_profit field is {}".format(min(total_profit)))  
    print("Max value in Total_profit field is {}".format(max(total_profit)))  
    print("Average Total_profit is {:.2f}".format(sum(total_profit) / len(total_profit)))
    
if __name__ == "__main__":
    print("Objects before reading CSV file : ",len(gc.get_objects()))
    read_file()    
    print("Objects after reading CSV file : ",len(gc.get_objects()))