# -----------------------------------------------------------------
# PyBank code
# -----------------------------------------------------------------

# import modules
import os
import csv

# path from this code to the csv
budget_csv = os.path.join("Resources", "budget_data.csv")

# variables & lists
total_dates = 0
net_profit_loss = 0
profits_losses = []
changes = []
dates = []



# open the file
with open(budget_csv) as csvfile: 
    
    # reader object
    csvreader = csv.reader(csvfile, delimiter = ',') 

    # skip header row
    next(csvreader)

    # read the rest of the rows 
    for row in csvreader: 
        
        # count the rows
        total_dates +=1

        # sum net profit or loss
        net_profit_loss += int(row[1])

        # add dates to list
        dates.append(row[0])

        # add profits/loss to a list
        profits_losses.append(int(row[1]))



# calculate profit/loss changes
for i in range(1, len(profits_losses)):
    change = profits_losses[i] - profits_losses[i - 1]
    changes.append(change)

# Calculate the average of the changes
average_change = round(sum(changes) / len(changes), 2)

# greatest increase and decrease
greatest_inc = max(changes)
greatest_dec = min(changes)


# dates of greatest increase and decrease
great_inc_date = dates[changes.index(greatest_inc) + 1]
great_dec_date = dates[changes.index(greatest_dec) + 1]



# print results
print("Financial Analysis")
print("------------------------------------------------------")
print(f"Total Months: {total_dates}")
print(f"Total: ${net_profit_loss}")
print(f"Average Change: ${average_change}")
print(f"Greatest Increase in Profits: {great_inc_date} (${greatest_inc})")
print(f"Greatest Decrease in Profits: {great_dec_date} (${greatest_dec})")


# lines to write in text file
lines = [
    "Financial Analysis\n",
    "------------------------------------------------------\n",
    f"Total Months: {total_dates}\n",
    f"Total: ${net_profit_loss}\n",
    f"Average Change: ${average_change}\n",
    f"Greatest Increase in Profits: {great_inc_date} (${greatest_inc})\n",
    f"Greatest Decrease in Profits: {great_dec_date} (${greatest_dec})\n",
]

# write text file
with open('output.txt', 'w') as file: 
    file.writelines(lines)

