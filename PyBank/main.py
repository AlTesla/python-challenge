import os
import csv
mounths = []
profit_losses = []
increase_decrease = []
csvpath = os.path.join('Resources','budget_data.csv')
textpath= os.path.join('analysis', 'budget_analysis.txt')
with open(csvpath) as csvfile_budget:
    csvreader = csv.reader(csvfile_budget, delimiter=',')
    next(csvreader)
    for row in csvreader:
        mounths.append(row[0])
        profit_losses.append(int(row[1]))
        
    increase_decrease = [(profit_losses[row] - profit_losses[row -1]) for row in range(1 , len(profit_losses))]
    mean = sum(increase_decrease)/len(increase_decrease)
    increase_decrease.insert(0,0)
    #mean = sum(increase_decrease)/len(increase_decrease)
    
    total_months =len(mounths)
    Total = sum(profit_losses)
    mean = round(mean, 2)
    #print(min(increase_decrease))
    #print(max(increase_decrease))
    #print(len(increase_decrease))
    dict_mounth_change = dict(zip(mounths, increase_decrease))
    #print(dict_mounth_change)
    max_key = max(dict_mounth_change, key=dict_mounth_change.get)
    min_key = min(dict_mounth_change, key=dict_mounth_change.get)
    max_change = [max_key, dict_mounth_change[max_key]]
    min_change = [min_key, dict_mounth_change[min_key]]

with open(textpath, 'w') as file:
    file.write(
        'Financial Analysis\n'
        '----------------------------\n'
        'Total Months:{}\n'
        'Total: {}\n'
        'Average Change:{}\n'
        'Greatest Increase in Profits:{}({})\n'      
        'Greatest Decrease in Profits:{}({})\n'.format(total_months, Total, mean,
                                                   max_change[0],max_change[1],
                                                   min_change[0],min_change[1])) 