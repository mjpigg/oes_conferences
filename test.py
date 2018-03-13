import csv

with open('pcr.csv','rU') as csvfile:
    data = csv.reader(csvfile, delimiter=',')
    next(data, None)
    conferences = []
    for row in data:
        conferences.append(row)


for l in conferences:
    print(l[0],l[1],l[6])