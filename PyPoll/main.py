import os
import csv

read_csv = os.path.join('election_data.csv')

total_votes = 0
candidate_list = []
candidate_dictionary = {}

with open(read_csv, newline='') as csvfile:

    csvreader = csv.reader(csvfile, delimiter =',')

    csv_header = next(csvreader)

    for row in csvreader:

        total_votes = total_votes + 1

        candidate_name = (row[2])
        if candidate_name not in candidate_list:
            candidate_list.append(candidate_name)
            candidate_dictionary[candidate_name] = 0
        else:
            candidate_dictionary[candidate_name] += 1
            
print("Election Results")
print("----------------------------------")
print(f"Total Votes: {total_votes}")
print("----------------------------------")
for candidate in candidate_dictionary:
    print(candidate + ":" + str(round(candidate_dictionary[candidate]/total_votes,2)*100) + "% (" + str(candidate_dictionary[candidate]) + ")")


fh = open('Election_Results_Complete', 'w')

fh.write("Election Results\n")
fh.write("----------------------------------\n")
fh.write(f"Total Votes: {total_votes}\n")
fh.write("----------------------------------\n")
for candidate in candidate_dictionary:
    fh.write(candidate + ":" + str(round(candidate_dictionary[candidate]/total_votes,2)*100) + "% (" + str(candidate_dictionary[candidate]) + ")")

fh.close()
