#http://www.anthonydebarros.com/2013/02/05/get-json-from-excel-using-python-xlrd/

import csv
from collections import OrderedDict
import json

temp_list = []

# Open the workbook
with open ('data_line.csv', 'rU') as f:
	reader = csv.reader(f, delimiter=';')
	# Iterate through rows, returning each as a list that you can index:
	for row in reader:
		days = OrderedDict()
		days['day'] = row[0]
		days['wind'] = row[1]
		days['temp'] = row[2]
		days['min_temp'] = row[3]
		days['neerslag'] = row[4]
	 	
		temp_list.append(days)

j = json.dumps(temp_list)
# Write to file
with open('data_ready.json', 'w') as f:
    f.write(j)

 





    
    
      
