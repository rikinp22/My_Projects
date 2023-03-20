import csv
import os

csvpath = os.path.join('Resources','budget_data.csv')

# Dependencies
      
net_total = []
month = []
avg_changes = []

# Read as reader and skip the header row

with open(csvpath, 'r') as csvfile:
    reader = csv.reader(csvfile, delimiter=',')
    
    header = next(reader)
    
# The total number of months included in the dataset

    for row in reader:
        month.append(row[0])
        net_total.append(int(row[1]))
    total_months = len(month)
           
          
    print("The total number of months included in the dataset is:", total_months)
    
# The net total amount of "Profit/Losses" over the entire period
      
    sum_net_total = sum(net_total)   
    print("The net total amount of Profit is:", sum_net_total)
    
# The changes in "Profit/Losses" over the entire period, and then the average of those changes
    x = 1
    y = 0
    profit_changes = (net_total[1] - net_total[0])
    for months in range(total_months-1):
        profit_changes = (net_total[x] - net_total[y])
        avg_changes.append(int(profit_changes))
        sum_avg_changes = sum(avg_changes)
        x+=1
        y+=1
    total_avg_change = sum_avg_changes/(total_months-1)
    print(total_avg_change)
    
    # The greatest increase in profits (date and amount) over the entire period

    # The greatest increase in profits (date and amount) over the entire period

    greatest_increase = max(avg_changes)
    change_max = avg_changes.index(greatest_increase)
    month_increased = month[change_max + 1]
    increase_amount = greatest_increase

    print(f"Greatest Increase in Profits: {month_increased} ({increase_amount: .0f}).")
       

# The greatest decrease in profits (date and amount) over the entire period

    greatest_decrease = min(avg_changes)
    change_min = avg_changes.index(greatest_decrease)
    month_decreased = month[change_min + 1]
    decrease_amount = greatest_decrease

    print(f"Greatest Decrease in Profits: {month_decreased} ({decrease_amount: .0f}).")    

# print the analysis to the terminal and export a text file with the results

analysis = (
    f"Financial Analysis\n"
    f"----------------------------\n"
    f"Total Months: {total_months}\n"
    f"Total: ${sum_net_total}\n"
    f"Greatest Increase in Profits: {month_increased} (${increase_amount: .0f}).\n"
    f"Greatest Decrease in Profits: {month_decreased} (${decrease_amount: .0f}).\n"
)

print(analysis)

# Export a text file with the results

analysis_export = "analysis/Financial_Analysis.txt"


with open(analysis_export,"w") as txt_file:
    txt_file.write(analysis)