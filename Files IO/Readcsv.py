#CSV File
#uses C:\PythonCodes\Student.csv

import csv
examplefile = open('c:\\pythoncodes\\student.csv')
examplereader = csv.reader(examplefile)
exampledata = list(examplereader)

print(exampledata)


for row in exampledata:
    print(str(row))
    
