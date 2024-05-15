import os
import csv

csvpath = r"C:\Users\jimmy\OneDrive\Documents\BootCamp_Challenges\PyBank\Resources\budget_data.csv"

total_profit_losses = 0
max_increase = 0
max_decrease = 0
max_increase_date = ""
max_decrease_date = ""
previous_profit_losses = None

with open(csvpath, encoding='UTF-8') as csvfile:
    csvreader = csv.reader(csvfile)
    #Store header
    header = next(csvreader)
    dates = []
    changes = []
    
    # Created a loop for rows in csvreader
    for row in csvreader:
        date = row[0]
        dates.append(date)
        profit_losses = int(row[1])
        total_profit_losses += profit_losses
        
        # Prompting to find the changed value in profit/loss 
        if previous_profit_losses is not None:
            change = profit_losses - previous_profit_losses
            changes.append(change)         

            # Find greatest increase in profit value & date
            if change > max_increase:
                max_increase = change
                max_increase_date = date

            # Find greatest decrease in profit value & date
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

# Results that will be in text
output_text = (
    "Financial Analysis\n"
    "                            \n"
    "----------------------------\n"
    "                            \n"
    f"Total Months: {total_months}\n"
    "                            \n"
    f"Total: ${total_profit_losses}\n"
    "                            \n"
    f"Average Change: ${round(average_change, 2)}\n"
    "                            \n"
    f"Greatest Increase in Profits: {max_increase_date} (${max_increase})\n"
    "                            \n"
    f"Greatest Decrease in Profits: {max_decrease_date} (${max_decrease})\n"
)

# Write the output to a text file
output_path = r"C:\Users\jimmy\OneDrive\Documents\BootCamp_Challenges\PyBank\analysis\Pybank_result.txt"
with open(output_path, 'w') as output_file:
    output_file.write(output_text)