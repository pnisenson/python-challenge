# import libraries
import os
import csv

# identify csv file to use
csvfile = os.path.join('Resources','election_data.csv')

# apply csv reader to file and identify header row
with open(csvfile) as budgfile:
	budgfile = csv.reader(budgfile, delimiter = ",")
	csvheader = next(budgfile)

# define Candidate lists to use for calculation and finding amounts
	candidate = []

# loop through Candidate row in CSV and add all values to Candidate list
	for row in budgfile:
		candidate.append(row[2])

# obtain total votes by counting the length of the list
	vote_count = len(candidate)
# use list comprehensions to search for each candidate in the candidate list and count the how many votes by candidate using len
	khan_votes = len([x for x in candidate if x == "Khan"])
	correy_votes = len([x for x in candidate if x == "Correy"])
	li_votes = len([x for x in candidate if x == "Li"])
	otooley_votes = len([x for x in candidate if x == "O'Tooley"])
# calculate percentage of votes by candidate
	khan_perc = round((khan_votes/vote_count)*100, 3)
	correy_perc = round((correy_votes/vote_count)*100, 3)
	li_perc = round((li_votes/vote_count)*100, 3)
	otooley_perc = round((otooley_votes/vote_count)*100, 3)	
# if statements to declare the winner of the election depending on who has the most votes
	if khan_votes > correy_votes and li_votes and otooley_votes:
		winner = "Khan"
	if correy_votes > khan_votes and li_votes and otooley_votes:
		winner = "Correy"
	if li_votes > khan_votes and correy_votes and otooley_votes:
			winner = "Li"
	if otooley_votes > khan_votes and correy_votes and li_votes:
			winner = "O'Tooley"

# print all required variables as Data Table
	print("Election Results")
	print("----------------------")
	print(f'Total Votes: {vote_count}')
	print("----------------------")
	print(f'Khan: {khan_perc}% ({khan_votes})')
	print(f'Correy: {correy_perc}% ({correy_votes})')
	print(f'Li: {li_perc}% ({li_votes})')
	print(f"O'Tooley: {otooley_perc}% ({otooley_votes})")
	print("----------------------")
	print(f'Winner: {winner}')

# create lists of candidate data outputs to write to file
	candidates = ['Khan','Correy','Li',"O'Tooley"]
	votes_by_cand = [khan_votes,correy_votes,li_votes,otooley_votes]
	voteperc_by_cand = [f'{khan_perc}%',f'{correy_perc}%',f'{li_perc}%',f'{otooley_perc}%']

# zip candidate data together
	cand_data = zip(candidates, voteperc_by_cand, votes_by_cand)

# use for loop to create report list in which each zipped detail is its own sublist
	report = []
	for x in cand_data:
		report.append(x)

# develop output path to write analysis.txt in the Analysis folder
output_path = os.path.join("Analysis","analysis.txt")

# open the output file in write mode
with open(output_path, "w", newline = '') as datafile:
	writer = csv.writer(datafile)
# create header row
	writer.writerow(['Candidate', f'% of Votes','Votes'])
# write file with each candidate's data on its own line
	writer.writerows(report)
# create row displaying total votes
	writer.writerow(['Total Votes:','',vote_count])
# create blank row
	writer.writerow([])
# create last row with winning candidate info
	writer.writerow([f'Winner: {winner}'])





