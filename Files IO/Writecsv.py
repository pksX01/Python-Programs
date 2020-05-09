#write CSV
#creates output.csv in c:\pythoncodes

import csv

outputFile = open('c:\\pythoncodes\\output1.csv','w',newline='')
outputWriter = csv.writer(outputFile)

outputWriter.writerow(['123','Vikas','2000'])
outputWriter.writerow(['124','Ajay','3000'])
outputWriter.writerow(['125','Vijay','4000'])
outputWriter.writerow(['126','Bhushan','5000'])

outputFile.close()

print('Done....')


