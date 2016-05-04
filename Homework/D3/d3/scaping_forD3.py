#http://www.anthonydebarros.com/2013/02/05/get-json-from-excel-using-python-xlrd/

import csv
from collections import OrderedDict
import json

countries_list = []

# Open the workbook
with open ('FIFAranking2.csv', 'rU') as f:
	reader = csv.reader(f, delimiter=';')
	# Iterate through rows, returning each as a list that you can index:
	for row in reader:
		countries = OrderedDict()
		countries['points'] = row[0]
		countries['country'] = row[1]
	 	
		countries_list.append(countries)

j = json.dumps(countries_list)
# Write to file
with open('barchart.json', 'w') as f:
    f.write(j)

 





    
    
      
