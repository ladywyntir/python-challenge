# Module 3 - Python Challenge PyBank -  Main.py
# Created by Marjorie Muñoz
#
# Create a Python script to analyze the voting data from election_data.csv. You must find:
#
#   - The total number of votes cast
#   - A complete list of candidates who received votes
#   - The percentage of votes each candidate won
#   - The total number of votes each candidate won
#   - The winner of the election based on popular vote
#
# Results should look like this:
# Election Results
# -------------------------
# Total Votes: 369711
# -------------------------
# Charles Casper Stockham: 23.049% (85213)
# Diana DeGette: 73.812% (272892)
# Raymon Anthony Doane: 3.139% (11606)
# -------------------------
# Winner: Diana DeGette
# -------------------------


import os   # import the module for operating systems
import csv  # import the module to read CSV files

# this sets a variable so we can reference the CSV source file
PyPollcsv = os.path.join('Resources', 'election_data.csv')

# sets the output file path and name
outputFile = os.path.join('analysis', "PyPoll_Analysis.txt")

# set the lists to store data from CSV
candidate = []
county = []

# dictionaries
candidate_votes = {}        # holds the candidates
county_count = {}           # holds the counties

# variables 
percent_of_vote = 0     # the percent of voters for a candidate
votes = 0               # total count of ballots cast
vote_count = 0          # total count of votes
most_votes = 0          # popular vote count
voter_output = ""       # holds the candidate to be printed in the results

#script to open as CSV file
with open(PyPollcsv) as voterCSV:
    #sets the variable for the delimiter that separates each piece of data
    csvreader = csv.reader(voterCSV, delimiter=',')

    csv_header = next(csvreader)    # reads the header row
    
    for row in csvreader:

        # increase ballot counter
        vote_count += 1        
      
        # check to see if the county is in the list of Counties
        if row[1] not in county:
            # if not already in the list, add it
            county.append(row[1])
            # add a counter for this county
            county_count[row[1]] = 1
        
        else:
            # if the county already exists
            county_count[row[1]] += 1

        # check to see if the candidate is in the list of Candidates
        if row[2] not in candidate:
            candidate.append(row[2])
            # add a counter for this candidate
            candidate_votes[row[2]] = 1
        else:
            # if the county already exists
            candidate_votes[row[2]] += 1


for candidate in candidate_votes:

        #get vote count and percent
        votes = candidate_votes.get(candidate)
        percent_of_vote = (float(votes) / float(vote_count)) * 100.00
        voter_output += f"{candidate}: {percent_of_vote:.3f}% ({votes}) \n"
           
        #compare votes to the winning count
        if votes > most_votes:
            most_votes = votes
            winning_candidate = candidate

most_votes_output = f"Winner: {winning_candidate}"

        

# displays results to the terminal window
output = (
    f" \n"
    f" \n"
    f"Election Results \n"
    f"\n-------------------------\n"
    f"\nTotal Votes: {vote_count}\n"
    f"\n------------------------- \n"
    f"\n{voter_output}"
    f"\n-------------------------\n"
    f"\n{most_votes_output}\n"
    f"\n-------------------------\n"
)

print(output)

# writes results to a text file
with open(outputFile, "w") as textFile:
    textFile.write(output)