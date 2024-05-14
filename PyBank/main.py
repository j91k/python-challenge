import os
import csv

csvpath = r"C:\Users\jimmy\OneDrive\Documents\BootCamp_Challenges\PyBank\Resources\budget_data.csv"

total_profit_losses = 0
previous_profit_losses = None
max_increase = 0
max_decrease = 0
max_increase_date = ""
max_decrease_date = ""


with open(csvpath, encoding='UTF-8') as csvfile:
    csvreader = csv.reader(csvfile)
    next(csvreader)
    dates = []
    changes = []

    for row in csvreader:
        date = row[0]
        dates.append(date)
        profit_losses = int(row[1])
        total_profit_losses += profit_losses
        
        
        if previous_profit_losses is not None:
            change = profit_losses - previous_profit_losses
            changes.append(change)

            if change > max_increase:
                max_increase = change
                max_increase_date = date

            if change < max_decrease:
                max_decrease = change
                max_decrease_date = date

        previous_profit_losses = profit_losses
        
unique_dates = set(dates)
total_months = len(unique_dates)
average_change = sum(changes) / len(changes)

print("Financial Analysis")
print("                            ")
print("----------------------------")
print("                            ")
print("Total Months:", total_months)
print("                            ")
print("Total: $" + str(total_profit_losses))
print("                            ")
print("Average Change: $" + str(round(average_change, 2)))
print("                            ")
print("Greatest Increase in Profits:", max_increase_date, "($" + str(max_increase) + ")")
print("                            ")
print("Greatest Decrease in Profits:", max_decrease_date, "($" + str(max_decrease) + ")")