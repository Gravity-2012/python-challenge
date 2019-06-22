import os
import csv
import collections

read_csv = os.path.join('election_data.csv')
largest = 0
winner = ""
total_votes = 0
candidate_list = []
candidate_dictionary = {}

with open(read_csv, newline='') as csvfile:

    csvreader = csv.reader(csvfile, delimiter =',')

    csv_header = next(csvreader)

    # Creating a counter object from the collecitons library
    candidate_count = collections.Counter()

    #gathering totals for each candidate
    for row in csvreader:

        total_votes += 1

        candidate_name = (row[2])
        
        # starts gathering names and check that there aren't any duplicates
        if candidate_name not in candidate_list:
            candidate_list.append(candidate_name)

        candidate_count[candidate_name] += 1

    candidate_dictionary = dict(candidate_count.most_common())

    #C = candidate name  v = votes associated with that candidate
    for c,v in candidate_dictionary.items():
        if v > largest:
            largest = v
            winner = c
            

    print(winner,str(largest))

print("Election Results")
print("----------------------------------")
print(f"Total Votes: {total_votes}")
print("----------------------------------")
for candidate,values in candidate_dictionary.items():
  
    print("%s: %.3f%% (%s)"%(str(candidate),(values/total_votes)*100,str(values)))
 
print("Winner: %s" % (winner)) 

fh = open('Election_Results_Complete', 'w')

fh.write("Election Results\n")
fh.write("----------------------------------\n")
fh.write(f"Total Votes: {total_votes}\n")
fh.write("----------------------------------\n")
for candidate,values in candidate_dictionary.items():
    fh.write("%s: %.3f%% (%s)"%(str(candidate),(values/total_votes)*100,str(values)))
    print("\n")

fh.write("\nWinner: " + winner)

fh.close()
