# Election_Analysis
## Project Overview
The Colorado Board of Elections has asked for an audit of a local congressional election. The asked for the following information:
1. Calculate the total number of votes cast.
2. List all the candidates that received votes.
3. Report the total number of votes for each of the candidates.
4. Report the percentage of the vote each candidate received.
5. Report the overall winner of the election based on popular vote.

## Resources
* Data Source: election_results.csv
* Software: Python 3.7.6, Visual Studio Code 1.63.2

## Summary
From the data provided, the following was found:

Total Votes: 369,711

Votes were received by these 3 candidates:
1. Charles Casper Stockham: 23.0% (85,213)
2. Diana DeGette: 73.8% (272,892)
3. Raymon Anthony Doane: 3.1% (11,606)

The Winner: Diana DeGette with 272,892 votes equaling 73.8% of the vote. 

## Challenge Overview
The challenge presented was to add county voting results to the analysis. It was requested that the total number of votes and percentages for each county would be reported and the county with the highest percentage voting identified as the county with the largest turnout.

To the for loop where I was already finding the candidate names and votes, I added a line to count county votes after an if statement to collect the unique county names. I then wrote those results to the election_analysis.txt file. The indenting of each block of code was my biggest issue in this challenge.  

## Challenge Summary
From the data provide, the following was found:

County Votes: 

Jefferson: 10.5% (38,855)

Denver: 82.8% (306,055)

Arapahoe: 6.7% (24,801)

Largest County Turnout: Denver 
