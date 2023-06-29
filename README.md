# python-challenge
this repository contains the python challenge assignment for Data Analytics Bootcamp 

## Scripting steps
First I began with creating the `python-challenge` repository on github, second i cloned the repository to my bootcamp folder, after I created the folders, empty files and droped the resources needed for the challenge, then I pushed them to the github repository, finally I start to code on the `main.py` files
## Coding the `PyBank`  
First, I began by dropping the libreries. Sencond I declared the Lists and the files' paths. Then, I opened `budget_data.csv` file and with a `for`, I gathered the data I needed from each row and performed calculations with the data. After that, I opened the output file in write mode and finally wrote the data to the output file  

```python
with open(csvpath) as csvfile_budget:
    csvreader = csv.reader(csvfile_budget, delimiter=',')
    next(csvreader)
    #gathering data from the csvfile
    for row in csvreader:
        months.append(row[0])
        profit_losses.append(int(row[1]))
    
    # creating new data     
    increase_decrease = [(profit_losses[row] - profit_losses[row -1]) 
                          for row in range(1 , len(profit_losses))]
    mean = sum(increase_decrease)/len(increase_decrease)
    #This script inserts a value at the first position of the ‘increase_decrease’
    #list to make it the same length as the ‘months’ list.
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

```
`List` comprehension example
## Coding the `pybank`
First I began by dropping the libreries. Second, I declared the lists and the files' paths. Then, I opened `election_data.csv` file and with a for loop I gathered the data I needed from each row and performed calculations with the data, I needed to write a dictionary `election_dir` with the amount of votes and the candidates' names. After that, I opened the output file in write mode and finally the data to the output file  
``` python
with open(csvpath) as csvfile_election:
    csvreader = csv.reader(csvfile_election, delimiter=",")
    next(csvreader)
    election_dir = {}
    #this loop writes a dictionary where 
    #canditate's names is the key and amount of votes is the value
    for row in csvreader:
        total += 1 
        key = row[2]
        if key in election_dir:
            election_dir[key] += 1
        else:
            election_dir[key] = 1
#looking the wiiner
max_key = max(election_dir, key=election_dir.get) 
```
