
import os
import csv
months = 0
total_profit = []
total_loss = []
change_in_rev = []
rev_list = []
prev_rev = []
date = row [0]
greatest_inc = []
#include date
greatest_dec = [0]
#include date
month_of_change = []
with open('Resources/budget_data.csv', 'r') as f:
   reader = csv.reader(f, delimiter=",")
   next(reader, None)
   for row in reader:
       months += 1
       total_profit.append(int(row[1])


# with open (csvpath, 'r') as f:
#    reader = csv.reader(f)
#    next(reader, None)
#    for row in reader:
#        months += 1
#        total_profit.append(int(row[1])
print(months)
print(total_profit)
