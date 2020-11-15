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
	
	for row in budgfile:
		# loops through second column in CSV and adds each amount
		tot_prof = tot_prof + int(row[1])
		# if function that if the cell in the first column isn't blank, count and add to month count
		if row[0] != "":
			mo_count = mo_count + 1
		#else: break
		revenue.append(int(row[1]))
		dates.append(row[0])
		

	# average change is:
	# (last month revenue - first month revenue)/(mos - 1)
	first_mo = int(revenue[0])
	last_mo = int(revenue[-1])
	avg_change = ((last_mo - first_mo)/(mo_count-1))
	revsht = revenue[1:]
	compsht = revenue[0:-1]
	combine = zip(revsht, compsht)
	combine_list = []
	for x , y in combine:
		combine_list.append(x-y)
	#mo_change = [revenue[1:])-int(comp_col[0:-1])]
	for x in combine_list:
		maxchgdex = combine_list.index(x) + 1
		if x == max(combine_list):
			break
	for x in combine_list:
		minchgdex = combine_list.index(x) + 1
		if x == min(combine_list):
			break

	maxdatedex = dates[maxchgdex]
	mindatedex = dates[minchgdex]
	
	print(combine_list)
	# print(revenue[1:])
	# print(comp_col[0:-1])
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
	print(f'Average Change: ${round(avg_change, 2)}')
	print(f'Greatest Increase: {maxdatedex} (${max(combine_list)})')
	print(f'Greatest Decrease: {mindatedex} (${min(combine_list)})')


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