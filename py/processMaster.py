#!/usr/bin/python

import csv
import re

datafile = open('/tmp/results.csv', 'r')
data = list(csv.reader(datafile))
title=data[0]
for row in data:
#	print row[0]
	if "File" in row[0]:
		filename=row[0].split('_')[1]
		major_no='{:03d}'.format(int(filename.split('-')[0]))
		minor_no='{:02d}'.format(int(filename.split('-')[1]))
		#print "major " + major_no + " minor " + minor_no
		row.insert(0, major_no + minor_no)

datafile.close()

data.sort(key=lambda x: x[0]);
with open('/tmp/masters.csv', 'wb') as csvfile:
	output = csv.writer(csvfile, dialect='excel')
	for i in range(len(title)):
		if i == 0:
			title[0]='CSV File'
		elif i == 5:
			title[i] ='Date of Birth'
		elif i == 6:
			title[i] = 'Place of Birth'
		elif i == 7:
			title[i] = 'Ship Number'
		elif i == 8:
			title[i] = 'Ship'
		elif i == 9:
			title[i] = 'Document Date'
		else:	
			title[i] = title[i].title()
	output.writerow(title)
	for row in data:
		if len(row) == 11:
			row.pop(0)
			row[0] = re.sub('.xml','',re.sub('file://','', row[0]))
			if len(row) == 10:
				row[9] = re.sub('T00:00:00.000Z','',row[9])
			else:
				print row
			output.writerow(row)

csvfile.close
