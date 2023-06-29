import os
import csv
#declare variables 
months = []
profit_losses = []
increase_decrease = []
#declare file's paths 
csvpath = os.path.join('Resources','budget_data.csv')
textpath= os.path.join('analysis', 'budget_analysis.txt')
# open csv file 
with open(csvpath) as csvfile_budget:
    csvreader = csv.reader(csvfile_budget, delimiter=',')
    next(csvreader)
    #gathering data from the csvfile
    for row in csvreader:
        months.append(row[0])
        profit_losses.append(int(row[1]))
    
    # creating new data     
    increase_decrease = [(profit_losses[row] - profit_losses[row -1]) for row in range(1 , len(profit_losses))]
    mean = sum(increase_decrease)/len(increase_decrease)
    #This script inserts a value at the first position of the ‘increase_decrease’ list to make it the same length as the ‘months’ list.
    increase_decrease.insert(0,0)
    #this dictionary relates the months with the increase or decrease
    dict_mounth_change = dict(zip(months, increase_decrease))
    max_key = max(dict_mounth_change, key=dict_mounth_change.get)
    min_key = min(dict_mounth_change, key=dict_mounth_change.get)
    #gathering the final data 
    total_months =len(months)
    Total = sum(profit_losses)
    mean = round(mean, 2)
    max_change = [max_key, dict_mounth_change[max_key]]
    min_change = [min_key, dict_mounth_change[min_key]]
#open the output file  
with open(textpath, 'w') as file:
    #writing the outfile 
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