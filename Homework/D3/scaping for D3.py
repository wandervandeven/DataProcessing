#Wander van de Ven 
#10470476

#https://docs.python.org/2/library/csv.html

import csv
from collections import OrderedDict
import json

countries_list = []

# Open de csv file
with open ('weather.csv', 'rU') as f:
	reader = csv.reader(f, delimiter=',')
	# Iterate through rows, returning each as a list that you can index:
	for row in reader:
		countries = OrderedDict()
		countries['day'] = row[0]
		countries['temp'] = row[1]
	 	
		countries_list.append(countries)

j = json.dumps(countries_list)
# Write to file
with open('barchart.json', 'w') as f:
    f.write(j)

 





    
    
      
