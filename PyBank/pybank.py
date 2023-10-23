import os
import csv

budget_csv = os.path.join("PyBank/Resources/budget_data.csv")

profit = []
total_months = 0
total_profit = 0
net_profit_loss = 0
revenue_change = []
dates = []

with open(budget_csv) as csvfile:
    csvread = csv.reader(csvfile, delimiter=",")
    header_csv = next(csvread)

    for row in csvread:
        
        dates.append(row[0])
        profit_loss = int(row[1])
        
        profit.append(row[1])
        total_months += 1
        total_profit = total_profit +int(row[1])

        if total_months > 1:
            change = profit_loss - net_profit_loss
            revenue_change.append(change)

        net_profit_loss = profit_loss


average_change = sum(revenue_change) / len(revenue_change)
average_change = str(round(average_change, 2))

maxinc = max(revenue_change)
maxdec = min(revenue_change)


max_increase_date = dates[revenue_change.index(maxinc) + 1]
max_decrease_date = dates[revenue_change.index(maxdec) + 1]


# Now print the results
print('Budget Data Analysis')
print('----------------------------------------------------')
print(f'Total months: {total_months}')
print(f'Total: ${total_profit}')
print(f'Average Change: ${average_change}')
print(f'Greatest Increase: {max_increase_date}(${maxinc})')
print(f'Greatest Decrease: {max_decrease_date}(${maxdec})')
print(f'---------------------------------------------------')

# Into txt
with open("PyBank/Resources/pybankanalysis.txt", "w") as text:
    text.write('Budget Data Analysis\n')
    text.write('-------------------------------------------------------\n')
    text.write(f'Total months: {total_months}\n')
    text.write(f'Total: ${total_profit}\n')
    text.write(f'Average Change: ${average_change}\n')
    text.write(f'Greatest Increase: {max_increase_date}(${maxinc})\n')
    text.write(f'Greatest Decrease: {max_decrease_date}(${maxdec})\n')
    text.write(f'------------------------------------------------------\n')