# Add our dependencies.
import csv
import os
# Assign a variable to load a file from a path.
file_to_load = os.path.join("Resources", "election_results.csv")
# Assign a variable to save the file to a path.
file_to_save = os.path.join("analysis", "election_analysis.txt")
#Initialize the vote counter, candidate options list, & candidate_votes dictionary.
total_votes=0
candidate_options=[]
candidate_votes={}
#Winning Candidate and Winning Count tracker.
winning_candidate=""
winning_count = 0
winning_per = 0
# Open the election results and read the file.
with open(file_to_load) as election_data:
    file_reader = csv.reader(election_data)

#read the header row.
    headers = next(file_reader)

#Count votes, collect candidate names, add unique names to candidate_options list.
    for row in file_reader:
        total_votes +=1
        candidate_name=row[2]
        if candidate_name not in candidate_options:
            candidate_options.append(candidate_name)
            candidate_votes[candidate_name]=0
        candidate_votes[candidate_name] +=1

#Print total votes.
#print(total_votes)
#print(candidate_options)
#print(candidate_votes)
#Iterate thru candidate list.
    for candidate_name in candidate_votes:
#retrieve votes counts per candidate.
        votes = candidate_votes[candidate_name]
#calcluate vote percentage per candidate.
        vote_per = float(votes)/float(total_votes) * 100
#print results for each candidate.
        print(f'{candidate_name}: {vote_per:.1f}% ({votes:,})')

#Determine winning vote count and candidate.
#Determine if the votes are greater than the winning count.
        if (votes > winning_count) and (vote_per > winning_per):
            winning_count = votes
            winning_per = vote_per
            winning_candidate = candidate_name
    winningSummary= (
        f'------------------------------\n'
        f'Winner: {winning_candidate} \n'
        f'Winning Vote Count: {winning_count:,}\n'
        f'Winning percentage: {winning_per:.1f}% \n')
    print(winningSummary)


