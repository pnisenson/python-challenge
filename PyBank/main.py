# import libraries
import os
import csv

# identify csv file to use
csvfile = os.path.join('Resources','budget_data.csv')

# apply csv reader to file and identify header row
with open(csvfile) as budgfile:
	budgfile = csv.reader(budgfile, delimiter = ",")
	csvheader = next(budgfile)

# create variable to sum profits and losses
	tot_prof = 0
# create variable to count the rows of CSV, with each row being a unique month
	mo_count = 0
# average change is:
	# (last month revenue - first month revenue)/(mos - 1)

# define lists to use for calculation and finding amounts: Revenue and Dates	
	revenue = []
	dates = []
	
# open loop to read csv file and: 1)add total profit 2)count months 3)transfer columns to lists
	for row in budgfile:
		# loops through second column in CSV and adds each amount
		tot_prof = tot_prof + int(row[1])
		# if function that if the cell in the first column isn't blank, count and add to month count
		if row[0] != "":
			mo_count = mo_count + 1
		# add column A of CSV to Dates list and column B of CSV to Revenue and Comparison Column lists
		revenue.append(int(row[1]))
		dates.append(row[0])

# identify profit/loss in first month of CSV and define as 'first_mo'
	first_mo = int(revenue[0])
# identify profit/loss in last month of CSV and define as 'last_mo'
	last_mo = int(revenue[-1])
# average change is:
## (last month revenue - first month revenue)/(mos - 1) (-1 because there is no change to the first month)
	avg_change = ((last_mo - first_mo)/(mo_count-1))
# define a new list "revsht" as the revenue column, but starting at the second row
	revsht = revenue[1:]
# define a new list "compare" as the revenue column, but ending a row before last
	compare = revenue[0:-1]
# zip the new lists together offsetting months revenue {month2rev, month1rev, month3rev, month2rev...}
	combine = zip(revsht, compare)
# define list to store the monthly change (the change between month 1 and month 2)
	mthly_change = []
# for month 2 revenue and month 1 revenue in the zip object, store Mo2 - Mo 1 in mthly_change
	for x , y in combine:
		mthly_change.append(x-y)
# indexes the monthly change and stops counting when it reaches the max (greatest increase). "+1" because the first monthly change occurs on the second row of dates
	for x in mthly_change:
		max_index = mthly_change.index(x) + 1
		if x == max(mthly_change):
			break
# indexes the monthly change and stops counting when it reaches the min (greatest decrease). "+1" because the first monthly change occurs on the second row of dates
	for x in mthly_change:
		min_index = mthly_change.index(x) + 1
		if x == min(mthly_change):
			break

# identifies the dates associated with the greatest increases and decreases
	maxdate = dates[max_index]
	mindate = dates[min_index]		

# print all required variables as Data Table
	print("Financial Analysis")
	print("----------------------")
	print(f'Total Months: {mo_count}')
	print(f'Total: ${tot_prof}')
	print(f'Average Change: ${round(avg_change, 2)}')
	print(f'Greatest Increase: {maxdate} (${max(mthly_change)})')
	print(f'Greatest Decrease: {mindate} (${min(mthly_change)})')

# create list of outputs to write to file
stats = ['Total Months','Total Profits/Losses','Average Change','Greatest Increase','Greatest Decrease']
solutions = [mo_count, tot_prof, round(avg_change,2), max(mthly_change), min(mthly_change)]
rel_date = ["","","",maxdate,mindate]
# zip answers together
answers = zip(stats, solutions, rel_date)
# use for loop to create report list in which each zipped detail is its own sublist
report = []
for x in answers:
	report.append(x)

# develop output path to write analysis.txt in the Analysis folder
output_path = os.path.join("Analysis","analysis.txt")

# open the output file in write mode
with open(output_path, "w", newline = '') as datafile:
	writer = csv.writer(datafile)
# create header row
	writer.writerow(['Statistic','Amount','Month, if applicable'])
# write file with each answer on its own line
	writer.writerows(report)