import os
import csv

read_csv = "PyBank.csv"

total = 0
total_months = 0
average_change_list = []
greatest_increase_in_profits = ["", 0]
greatest_decrease_in_profits = ["", 9999999999]

with open(read_csv, newline='') as csvfile:

    csvreader = csv.reader(csvfile, delimiter =',')

    csv_header = next(csvreader)

    first_row = next(csvreader)
    previous = int(first_row[1])
    total = total + int(first_row[1])
    total_months = total_months + 1

    for row in csvreader:
        total_months = total_months + 1
        total = total + int(row[1])
        average_change = int(row[1]) - previous
        average_change_list = average_change_list + [average_change]
        previous = int(row[1])

        if average_change > greatest_increase_in_profits[1]:
            greatest_increase_in_profits[0] = row[0]
            greatest_increase_in_profits[1] = average_change

        if average_change < greatest_decrease_in_profits[1]:
            greatest_decrease_in_profits[0] = row[0]
            greatest_decrease_in_profits[1] = average_change

total_monthly_average = sum(average_change_list) / len(average_change_list)

print("Financial Analysis")
print("----------------------------------")
print(f"Total Months: {total_months}")
print(f"Total:  ${total}")
print(f"Average Change: ${total_monthly_average}")
print(f"Greatest Increase in Profits: {greatest_increase_in_profits}")
print(f"Greatest Decrease in Profits: {greatest_decrease_in_profits}")

output_path = os.path.join("..", "PyBank", "Financial_Analysis_Complete.csv")

with open(output_path, 'w', newline='') as csvfile:
    csvwriter = csv.writer(csvfile, delimiter=',')

    csvwriter.writerow(["Financial Analysis"])
    csvwriter.writerow(['----------------------------'])
    csvwriter.writerow([f"Total Months: {total_months}"])
    csvwriter.writerow([f"Total: ${total}"])
    csvwriter.writerow([f"Average Change: ${total_monthly_average}"])
    csvwriter.writerow([f"Greatest Increase in Profits: {greatest_increase_in_profits}"])
    csvwriter.writerow([f"Greatest Decrease in Profits: {greatest_decrease_in_profits}"])
