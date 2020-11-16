# import libraries
import os
import csv

# identify csv file to use
csvfile = os.path.join('Resources','election_data.csv')

# apply csv reader to file and identify header row
with open(csvfile) as budgfile:
	budgfile = csv.reader(budgfile, delimiter = ",")
	csvheader = next(budgfile)

	
	voterid = []
	county = []
	candidate = []

	for row in budgfile:
		voterid.append(row[0])
		county.append(row[1])
		candidate.append(row[2])

	vote_count = len(voterid)
	khan_votes = len([x for x in candidate if x == "Khan"])
	correy_votes = len([x for x in candidate if x == "Correy"])
	li_votes = len([x for x in candidate if x == "Li"])
	otooley_votes = len([x for x in candidate if x == "O'Tooley"])
	khan_perc = round(float((khan_votes/vote_count)*100), 3)
	correy_perc = round((correy_votes/vote_count)*100, 4)
	li_perc = round((li_votes/vote_count)*100, 4)
	otooley_perc = round((otooley_votes/vote_count)*100, 4)

	xyz = round(12.4355677854,3)

	#[vote == 1 for vote in voterid if vote != ""]


	print(xyz)



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
