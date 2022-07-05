# Module 3 - Python Challenge PyBank -  Main.py
# Created by Marjorie Muñoz
#
# Create a Python script to analyze the financial records of your company. Use the csv budget_data.csv
# in the resources folder. You must find:
#   - Total months in dataset  
#   - Net total amount of "Profit/Losses"
#   - Changes in "Profit/Losses" over entire period
#   - Greatest increase in profits (date and amount)
#   - Greatest decrease in profits (date and amount)
#
# Results should look like this:
#   Financial Analysis
#   ----------------------------
#   Total Months: 86
#   Total: $22564198
#   Average Change: $-8311.11
#   Greatest Increase in Profits: Aug-16 ($1862002)
#   Greatest Decrease in Profits: Feb-14 ($-1825558)
#
# The analysis should be displayed in terminal and exported to a text file.
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~



import os   # import the module for operating systems
import csv  # import the module to read CSV files

# this sets a variable so we can reference the CSV source file
PyBankcsv = os.path.join('Resources','budget_data.csv')

# sets the output file path and name
outputFile = os.path.join('analysis',"PyBank_Analysis.txt" )

# set the lists to store data from CSV
date = []
profit_losses = []
changes_monthly = [] 

# Variables for the calculations below (set those variables!)
profitloss_initial = 0      # sets the initial profit/loss value to 0
profitloss_change = 0       # sets the change of profit/loss to 0
profitloss_current = 0      # sets the current revenue to 0
profitloss_net = 0          # sets the profit/loss net to 0
month_count = 0             # sets the monthly count to 0

# script to open as CSV file
with open(PyBankcsv) as csvfile:

    # sets the variable for the delimiter that separates each piece of data
    csvreader = csv.reader(csvfile, delimiter=',')

    csv_header = next(csvreader)    # reads the header row
    firstRow = next(csvreader)      # reads the first data row
    month_count += 1                # starts the counter for # of months

    # add total profitloss
    profitloss_current += float(firstRow[1]) 

    # previous profit/loss amount 
    profitloss_initial = float(firstRow[1])

    #setting the initial amount to begin the Net calculation
    profitloss_net = float(firstRow[1])

    # reads each row after the header
    for row in csvreader:
        # enter date into row
        date.append(row[0])   
        
        # increase month counter
        month_count += 1
       
        # add total revenue
        profitloss_net += float(row[1])

        # enter profit_losses into row
        profit_losses.append(row[1])

        #calculations
        profitloss_monthly_change = float(row[1]) - profitloss_initial  # change profits/losses

        # store the profit change in the "changes_monthly" list
        changes_monthly.append(profitloss_monthly_change)  

        # replacing the initial change value with the latest one
        profitloss_initial = float(row[1]) 

       
    #calculating length of date list
    date_count = len(date)
# calculate average net change
profitloss_avg_change = sum(changes_monthly)/len(changes_monthly)


# Max and Mins of Profits and Dates
profit_increase = int(max(changes_monthly))                # set the greatest profit increase
loss_decrease = int(min(changes_monthly))                  # set the greatest loss decrease
date_increase = date[changes_monthly.index(profit_increase)]  # set the date for the greatest increase
date_decrease = date[changes_monthly.index(loss_decrease)]    # set the date for the greatest decrease

    
# generate output
output = (
    f" \n"
    f"\nFinancial Analysis \n"
    f"----------------------------\n"
    f"\tTotal Months: {month_count} \n"
    f"\tNet Total: ${profitloss_net:,.2f}\n"
    f"\tAverage Change: ${profitloss_avg_change:,.2f}\n"
    f"\tGreatest Increase in Profits: {date_increase} - (${profit_increase})\n"
    f"\tGreatest Decrease in Profits: {date_decrease} - (${loss_decrease})\n"
)
    
# display output in terminal
print(output)

    
# export the results into a text file
with open(outputFile, "w") as textFile:
    textFile.write(output)




    


