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
	
	first_mo = 0
	revenue = []
	dates = []
	comp_col = []
	for row in budgfile:
		# loops through second column in CSV and adds each amount
		tot_prof = tot_prof + int(row[1])
		# if function that if the cell in the first column isn't blank, count and add to month count
		if row[0] != "":
			mo_count = mo_count + 1
		else: break
		revenue.append(row[1])
		dates.append(row[0])
		comp_col.append(row[1])
	# average change is:
	# (last month revenue - first month revenue)/(mos - 1)
	first_mo = int(revenue[0])
	last_mo = int(revenue[-1])
	avg_change = ((last_mo - first_mo)/(mo_count-1))
	#comp_col.append((revenue[0]))
	#comp_col.append(revenue)
	
	print((revenue[1:]))
	print(comp_col[0:-1])
	# for x in revenue:
	# 	print(f'{x}')

	# for x in budgfile:
	# 	if x[1] != "":
	# 		first_mo = first_mo + int(x[1])
	# 	else: first_mo = first_mo + 2000

			
			
		

	
	print("Financial Analysis")
	print("----------------------")
	print(f'Total Months: {mo_count}')
	print(f'Total: ${tot_prof}')
	print(f'Average Change: ${int(avg_change)}')
	#print(f'Greatest Increas: ${int(month_chg)}')