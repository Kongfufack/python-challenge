import os
import csv

budget_data_csv = os.path.join("..", "Resources", "budget_data.csv")

total_months = 0
total_profit = 0
prev_profit = 0
profit_change = 0
greatest_increase = ["", 0]
greatest_decrease = ["", 9999999]
profit_changes = []


with open(budget_data_csv) as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=",")

    next(csv_reader)

    for row in csv_reader:
        date = row[0]
        profit = int(row[1])

        total_months += 1
        total_profit += profit

        if prev_profit != 0:
            profit_change = profit - prev_profit
            profit_changes.append(profit_change)

            if profit_change > greatest_increase[1]:
                greatest_increase[0] = date
                greatest_increase[1] = profit_change

            if profit_change < greatest_decrease[1]:
                greatest_decrease[0] = date
                greatest_decrease[1] = profit_change

        prev_profit = profit

average_change = sum(profit_changes) / len(profit_changes)

print(f"Total Months: {total_months}")
print(f"Total Profit: ${total_profit}")
print(f"Average Change: ${average_change:.2f}")
print(f"Greatest Increase in Profits: {greatest_increase[0]} (${greatest_increase[1]})")
print(f"Greatest Decrease in Profits: {greatest_decrease[0]} (${greatest_decrease[1]})")

with open("../analysis/results.txt", "w") as f:
    f.write(f"Total months: {total_months}\n")
    f.write(f"Total: ${total_months}\n")
    f.write(f"Average change: ${average_change:.2f}\n")
    f.write(f"Greatest increase in profits: {greatest_increase[0]} (${greatest_increase[1]})\n")
    f.write(f"Greatest decrease in profits: {greatest_decrease[0]} (${greatest_decrease[1]})\n")