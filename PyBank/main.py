import os
import csv


#identify csv file
csvfile = os.path.join('Resources','budget_data.csv')


with open(csvfile) as budgfile:
	budgfile = csv.reader(budgfile, delimiter = ",")
	csvheader = next(budgfile)


	tot_prof = 0
	mo_count = 0
# create variable to count the rows of CSV, with each row being a unique month
	for row in budgfile:
		tot_prof = tot_prof + int(row[1])
		if row[0] != "":
			mo_count = mo_count + 1

	
	print("Financial Analysis")
	print(f'Total Months: {mo_count}')
	print(f'Total: {tot_prof}')