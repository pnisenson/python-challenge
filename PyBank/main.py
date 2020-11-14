import os
import csv


#identify csv file
csvfile = os.path.join('Resources','budget_data.csv')


with open(csvfile) as budgfile:
	budgfile = csv.reader(budgfile, delimiter = ",")
	csvheader = next(budgfile)

# create variable to sum profits and losses
	tot_prof = 0
# create variable to count the rows of CSV, with each row being a unique month
	mo_count = 0
# average change is:
	# (last month revenue - first month revenue)/(mos - 1)
	change = 0
	first_mo = 0
	new_list = []
	for row in budgfile:
		# loops through second column in CSV and adds each amount
		tot_prof = tot_prof + int(row[1])
		# if function that if the cell in the first column isn't blank, count and add to month count
		if row[0] != "":
			mo_count = mo_count + 1
		else: break
		new_list.append(row[1])
	print(int(new_list[0]))
	print(int(new_list[mo_count-1]))

	# for x in budgfile:
	# 	if x[1] != "":
	# 		first_mo = first_mo + int(x[1])
	# 	else: first_mo = first_mo + 2000

			
			
		

	
	print("Financial Analysis")
	print(f'Total Months: {mo_count}')
	print(f'Total: {tot_prof}')
	#print(f'Average Change: {change/(mo_count - 1)}')