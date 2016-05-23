file = open('temp.ini', 'r')

string = ""
path = ""
definition = ""
settings = ""

array = []
rows = ("Aliases", "Default", "Definition")
array.append(rows);

for line in file:
	string = line.strip()
	
	if string == "":
		# Empty line
		continue

	if string[0] == ';':
		# definition
		definition = definition + string[1:] + " "
	elif string[0] == '[':
		# settings path
		path = string[1:-1] + "."
	else:
		# parse settings
		arr = string.split('=')
		left = arr[0].strip()
		right = arr[1].strip()

		# append settings
		array.append((path + left, right, definition))

		# reset 
		left = ""
		right = ""
		definition = ""

import csv

outfile = open("output.csv", "wb")
output = csv.writer(outfile, delimiter = ",", quoting = csv.QUOTE_ALL)

for i in array:
	output.writerow(i)
