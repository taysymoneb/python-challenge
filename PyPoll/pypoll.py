import os
import csv

#load file to read poll data 
INPUT_CSV_PATH = os.path.join("Resources", "election_data.csv")

#ouput file location for PyPoll Analysis
outputFile = os.path.join("pypollAnalysis.txt")

totalVotes = 0 #holds the total number of votes
name = [] #holds the candidate names in the poll
candidateVotes = {}
winningCount = 0 #hold the winning count
winningCandidate = ""

os.chdir(os.path.dirname(os.path.realpath(__file__)))
with open(INPUT_CSV_PATH) as input_csv_file:
    csvreader = csv.reader(input_csv_file)
    #read the header
    header = next(csvreader)
  
    #index 0 is the ballot ID
    #index 1 is the county
    #index 2 is the candidate 

#loop through each row(list)
    for row in csvreader:
        #add to total votes
        totalVotes += 1

        if row[2] not in name:
            #if the candidate name is not in the list of candidate names
           name.append(row[2])
            #add that candidate to the candidate names list and initialize to index 1
           candidateVotes[row[2]] = 1
        else:
            #add a vote to the vote count
           candidateVotes[row[2]] +=1

voteOutput = ""

for name in candidateVotes:
#get vote count and percentage of votes
    votes = candidateVotes.get(name)
    votePct = float(votes)/float(totalVotes)*100.00
    voteOutput += f"\n{name}: {votePct:.2f}% ({votes})\n"
  
    #if statement to calculate the winning candidate
    if votes > winningCount:
       
       winningCount = votes
       winningCandidate = name
#winning candidate ouput variable
winningCandidateOutput =f"Winner: {winningCandidate}\n"

#create ouput variable to hold outputs for analysis txt file
output = (
    f"\n\nElection Results\n"
    f"---------------------------\n"
    f"Total Votes: {totalVotes}\n"
    f"---------------------------\n"
    f"{voteOutput}\n"
    f"---------------------------\n"
    f"{winningCandidateOutput}"
    f"---------------------------\n"
)

print(output)

with open(outputFile, "w") as textfile:
    textfile.write(output)
