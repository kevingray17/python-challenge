import csv
import os

#   Variable that points to the file
file_path="Resources/budget_data.csv"
total_months=0
total_profit=0
previous_month=0
average_change=0
list_changes=[]
largest_increase=0
largest_increase_month=""     
largest_decrease=0
largest_decrease_month=""           
with open(file_path) as csvfile:

    # CSV reader specifies delimiter and variable that holds contents
    csvreader = csv.reader(csvfile, delimiter=',') 

    # Read the header row first (skip this step if there is now header)
    next(csvreader,None)
    # Read each row of data after the header
    for x in csvreader:
            current_change = int(x[1]) - previous_month
            total_months = total_months + 1
            total_profit = total_profit + int(x[1])
            previous_month = int(x[1])
            list_changes.append(current_change) 
            if largest_increase < current_change:
                largest_increase = current_change 
                largest_increase_month = x[0]    
            if largest_decrease > current_change:
                largest_decrease = current_change
                largest_decrease_month = x[0]

#   The total number of months included in the dataset
print(total_months)
average_change = sum(list_changes) / total_months

#   The net total amount of "Profit/Losses" over the entire period
print(total_profit)

#   The average of the changes in "Profit/Losses" over the entire period
print(average_change)
#   The greatest increase in profits (date and amount) over the entire period
print(largest_increase_month)
#   The greatest decrease in losses (date and amount) over the entire period
print(largest_decrease_month)

Output= f"Total number of months are{total_months}\n" \
        f"Total profits are ${total_profit}\n" \
        f"Average change each month is ${average_change}\n" \
        f"The largest monthly increase in profits totaled $ {largest_increase} which occured in {largest_increase_month}\n" \
        f"The greatest monthly decrease in profits totaled $ {largest_decrease} which occured in {largest_decrease_month}\n"


print (Output)
# Set variable for output file
output_file = "./Analysis/summary.txt"
#  Open the output file
with open(output_file, "w", newline='') as datafile:
    datafile.write(Output)
    