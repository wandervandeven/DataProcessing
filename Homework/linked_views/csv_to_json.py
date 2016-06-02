#http://www.anthonydebarros.com/2013/02/05/get-json-from-excel-using-python-xlrd/

import csv
from collections import OrderedDict
import json

temp_list = []




# Open the workbook
with open ('data2.csv', 'rU') as f:
	reader = csv.reader(f, delimiter=';')
	# Iterate through rows, returning each as a list that you can index:
	for row in reader:
		days = OrderedDict()
		days['country'] = row[0]
		days['in_2003'] = row[1]
		days['out_2003'] = row[2]
		days['in_2006'] = row[3]
		days['out_2006'] = row[4]
		days['in_2009'] = row[5]
		days['out_2009'] = row[6]
		days['in_2012'] = row[7]
		days['out_2012'] = row[8]
	 	
		temp_list.append(days)

j = json.dumps(temp_list)
# Write to file
with open('students_ready.json', 'w') as f:
    f.write(j)

 





    
    
      
