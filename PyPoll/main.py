import os
import csv
total = 0
csvpath = os.path.join('Resources', 'election_data.csv')
textpath= os.path.join('analysis', 'election_analisis.txt')

with open(csvpath) as csvfile_election:
    csvreader = csv.reader(csvfile_election, delimiter=",")
    next(csvreader)
    election_dir = {}
    for row in csvreader:
        total += 1 
        key = row[2]
        if key in election_dir:
            election_dir[key] += 1
        else:
            election_dir[key] = 1

max_key = max(election_dir, key=election_dir.get) 

with open(textpath, 'w') as output_file:
    output_file.write('Election Results\n'
                      '-------------------------\n'
                      'Total Votes: {}\n'
                      '-------------------------\n'.format(total))
    for key, value in election_dir.items():
        percentage = (100*value/total)
        percentage = round(percentage, 3)      
        output_file.write("{}: {}% ({}) \n".format(key, percentage, value))
    output_file.write('-------------------------\n'
                      'Winner: {}\n'
                      '-------------------------\n'.format(max_key))                  
 # printing resoults on terminal   
print(
    '\nElection Results\n'
    '-------------------------\n'
    'Total Votes: {}\n'
    '-------------------------\n'.format(total)   
    )
for key, value in election_dir.items():
    percentage = (100*value/total)
    percentage = round(percentage, 3)      
    print("{}: {}% ({}) \n".format(key, percentage, value))
print('-------------------------\n'
      'Winner: {}\n'
      '-------------------------\n'.format(max_key))   