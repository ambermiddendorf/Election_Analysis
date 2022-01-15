# Add our dependencies.
import csv
import os

# Assign a variable to load a file from a path.
file_to_load = "C:/Users/amber/Classwork/Election_Analysis/Resources/election_results.csv"
#file_to_load = os.path.join("Resources", "election_results.csv")
# Assign a variable to save the file to a path.
file_to_save = "C:/Users/amber/Classwork/Election_Analysis/analysis/election_analysis.txt"
#file_to_save = os.path.join("analysis", "election_analysis.txt")
#Initialize the vote counter, candidate options list, & candidate_votes dictionary.
total_votes=0
candidate_options=[]
candidate_votes={}
#Winning Candidate and Winning Count tracker.
winning_candidate=""
winning_count = 0
winning_per = 0
#County Counts trackers.
county_options=[]
county_votes={}
#Winning county tracker.
c_winning_count=0
c_winning_per=0
c_winning_county=""
# Open the election results and read the file.
with open(file_to_load) as election_data:
    file_reader = csv.reader(election_data)

#read the header row.
    headers = next(file_reader)

#Count votes, 
    for row in file_reader:
        total_votes +=1
        candidate_name=row[2]
        county_name=row[1]
#collect candidate names, add unique names to candidate_options list, count votes for each candidate.
        if candidate_name not in candidate_options:
            candidate_options.append(candidate_name)
            candidate_votes[candidate_name]=0
        candidate_votes[candidate_name] +=1
#collect county names, add unique names to county_options and count votes for each county.
        if county_name not in county_options:
            county_options.append(county_name)
            county_votes[county_name]=0
        county_votes[county_name] +=1

#Save results to file.
with open(file_to_save, "w") as txt_file:
#print the final vote count to the terminal.
    election_results=(
        f'\nElection Results\n'
        f'--------------------------\n'
        f'Total Votes: {total_votes:,}\n'
        f'---------------------------\n')

    print(election_results, end="")
#Save the final vote count to the text file.
    txt_file.write(election_results)
    txt_file.write("County Votes: \n")
    print("County Votes: ")

    for county_name in county_votes:
#retrieve votes counts per county.
        c_votes = county_votes[county_name]
#calcluate vote percentage per county.
        c_vote_per = float(c_votes)/float(total_votes) * 100
#print results for each county.
        county_results = (
        f'{county_name}: {c_vote_per:.1f}% ({c_votes:,})\n')
# Print each county, their voter count, and percentage to the terminal.
        print(county_results)
#  Save the county results to our text file.
        txt_file.write(county_results)
#Determine the winning County        
        if (c_votes > c_winning_count) and (c_vote_per > c_winning_per):
            c_winning_count = c_votes
            c_winning_per = c_vote_per
            c_winning_county = county_name
    c_winningSummary= (
        f'------------------------------\n'
        f'Largest County Turnout: {c_winning_county} \n'
        f'-------------------------------\n')

    print(c_winningSummary)
#Save the winning county's results to the text file.
    txt_file.write(c_winningSummary)

    #Iterate thru candidate list.
    for candidate_name in candidate_votes:
    #retrieve votes counts per candidate.
        votes = candidate_votes[candidate_name]
    #calcluate vote percentage per candidate.
        vote_per = float(votes)/float(total_votes) * 100
    #print results for each candidate.
        candidate_results = (f'{candidate_name}: {vote_per:.1f}% ({votes:,})\n')
# Print each candidate, their voter count, and percentage to the terminal.
        print(candidate_results)
#  Save the candidate results to our text file.
        txt_file.write(candidate_results)
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
#Save the winning candidate's results to the text file.
    txt_file.write(winningSummary)

