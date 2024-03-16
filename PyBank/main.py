import os
import csv

budget_data = os.path.join("Resources", "budget_data.csv")

with open(budget_data) as csvfile:
    csv_reader = csv.reader(csvfile, delimiter=",")
    next(csv_reader)
    count = 0
    total = 0
    average_change = 0
    profit = []
    profit_per_month =[]
    month = []

    for row in csv_reader:
        count += 1
        total = total + int(row[1])

        #Puts row[1] into profit, row[0] into month
        profit.append(row[1])
        month.append(row[0])

#The range of len(profit) is 86 because there are 86 months == 86 profits. -1 because we need 85 as there are 85 changes out of the 86 profits
    for i in range(len(profit)-1):
        profit_per_month.append(int(profit[i+1]) - int(profit[i]))

    average_change = sum(profit_per_month) / (count - 1) #Count - 1 gives us 85 months because there are 85 total changes out of 86 months
    average_change = round(average_change, 2) #rounds the output to a decimal of 2

    #Max used to find the maximum value in the list "profit_per_month", same thing for min for minimum
    high_profit = max(profit_per_month)
    low_profit = min(profit_per_month)
    max_profit_date = profit_per_month.index(max(profit_per_month))
    min_profit_date = profit_per_month.index(min(profit_per_month))

print("Financial Analysis")
print("----------------------------")
print(f"Total Months = {count}")
print(f"Total = ${total}")
print(f"Average Change = ${average_change}")
print(f"Greatest Increase in Profits: {month[max_profit_date + 1]} (${high_profit})")
print(f"Greatest Decrease in Profits: {month[min_profit_date + 1]} (${low_profit})")
