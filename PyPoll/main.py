# -----------------------------------------------------------------
# PyPoll code
# -----------------------------------------------------------------

#import modules
import os
import csv
from collections import defaultdict

# path from this code to the csv
election_csv = os.path.join("Resources", "election_data.csv")

# variables
total_votes = 0
candidate_votes = defaultdict(int)



# open the file
with open(election_csv) as csvfile: 
    
    # reader object
    csvreader = csv.reader(csvfile, delimiter = ',') 

    # skip header row
    header = next(csvreader)

    # Determine the index of the column containing candidate names
    candidate_index = header.index('Candidate')

    # read the rest of the rows 
    for row in csvreader: 

        # count total votes
        total_votes += 1

        # add unique candidate names to dict and increment vote count 
        candidate_name = row[candidate_index]
        candidate_votes[candidate_name] += 1  

# Convert the defaultdict to a regular dictionary
candidate_dict = dict(candidate_votes)

# Calculate the winner
winner = max(candidate_dict, key=candidate_dict.get)
# max_votes = candidate_dict[winner]

# print total votes
print("------------------------------------------------")
print("Election Results")
print("------------------------------------------------")
print(f"Total Votes: {total_votes}")
print("------------------------------------------------")
# Print the dictionary with candidate names, percent of votes, and vote counts
for candidate, votes in candidate_dict.items():
    percentage = round((votes / total_votes) * 100, 3)
    print(f"{candidate}: {percentage}% ({votes}) votes")
print("------------------------------------------------")
print(f"Winner: {winner}")
print("------------------------------------------------")



# open and write text file
output_file = "election_results.txt"
with open(output_file, 'w') as file:
    file.write("------------------------------------------------\n")
    file.write("Election Results\n")
    file.write("------------------------------------------------\n")
    file.write(f"Total Votes: {total_votes}\n")
    file.write("------------------------------------------------\n")
    
    # Write candidate names, percent of votes, and vote counts from dictionary
    for candidate, votes in candidate_dict.items():
        percentage = round((votes / total_votes) * 100, 3)
        file.write(f"{candidate}: {percentage}% ({votes} votes)\n")
    
    file.write("------------------------------------------------\n")
    file.write(f"Winner: {winner}\n")
    file.write("------------------------------------------------\n")

