# First we'll import the os module
# This will allow us to create file paths across operating systems
import os

# Module for reading CSV files
import csv

# Define path to csv file
csvpath = os.path.join('..', 'budget_data.csv')

month_count = 0
net_amount = 0

# Convert path into a file
with open(csvpath, newline='') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')

    csv_header = next(csvreader)

    for row in csvreader:
        
        # Total number of months included in dataset
        month_count += 1
        
        # Total net amount of "Profits/Losses" over the entire period
        net_amount += (int(row[1]))

        # Average change in "Profit/Losses" between months over the entire period
        # Greatest increase in profits (date and amount) over the entire period
        # Greatest decrease in losses (date and amount) over the entire period


print("Financial Analysis")
print("-----------------------------------")
print("Total Months: " + (str(month_count)))
print("Total: $" +(str(net_amount)))




