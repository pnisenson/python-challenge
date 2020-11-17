#####DO NOT USE THIS FILE IN GRADING OF HOMEWORK. USED WITH MAIN.PY TO TEST VARIOUS CODE IDEAS OUT#####
#####DO NOT USE THIS FILE IN GRADING OF HOMEWORK. USED WITH MAIN.PY TO TEST VARIOUS CODE IDEAS OUT#####
#####DO NOT USE THIS FILE IN GRADING OF HOMEWORK. USED WITH MAIN.PY TO TEST VARIOUS CODE IDEAS OUT#####

# import libraries
import os
import csv

# identify csv file to use
csvfile = os.path.join('Resources','budget_data.csv')

# apply csv reader to file and identify header row
with open(csvfile) as budgfile:
	budgfile = csv.reader(budgfile, delimiter = ",")
	csvheader = next(budgfile)

# define lists to use for calculation and finding amounts: Revenue and Dates	
	revenue = []
	dates = []
	
# open loop to read csv file and: 1)add total profit 2)count months 3)transfer columns to lists
	for row in budgfile:
		# add column A of CSV to Dates list and column B of CSV to Revenue and Comparison Column lists
		revenue.append(int(row[1]))
		dates.append(row[0])

# create variable to sum profits and losses
	tot_prof = sum(revenue)
# create variable to count the rows of CSV, with each row being a unique month
	mo_count = len(dates)
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

	profloss = sum(revenue) 
	print(profloss)

# print all required variables as Data Table
	print("Financial Analysis")
	print("----------------------")
	print(f'Total Months: {mo_count}')
	print(f'Total: ${tot_prof:,}')
	print(f'Average Change: ${round(avg_change, 2):,}')
	print(f'Greatest Increase: {maxdate} (${max(mthly_change):,})')
	print(f'Greatest Decrease: {mindate} (${min(mthly_change):,})')

	

	# print(revenue[1:])
	# print(comp_col[0:-1])
	# for x in revenue:
	# 	print(f'{x}')

	# for x in budgfile:
	# 	if x[1] != "":
	# 		first_mo = first_mo + int(x[1])
	# 	else: first_mo = first_mo + 2000



# #to combine lists and subtract
# combo_list = []
# list1 = [1,2,3]
# list2 = [10,15,20]
# combo = zip(list1,list2)
# print(combo)
# for x , y in combo:
# 	print(x - y)
# 	combo_list.append(x -y)
# print(combo_list)
# #print max and min
# print(max(combo_list))
# print(min(combo_list))