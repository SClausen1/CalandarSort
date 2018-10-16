from bipartiteMatch import bipartiteMatch
#import numpy as np
import csv

data = {}

with open('SampleData.csv') as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',')

    for row in csv_reader:
        data[row[0]] = row[1:]

        matching = {}
        for name1 in data:
            for name2 in data:
                for v in data[name1]:
                    for v2 in data[name2]:
                        if name1 != name2 and v == v2:
                            matching[v] = name1, name2
                            break


    #    unique = {}
    #    for u in matching:
    #        if matching[u] in unique:
    #            break
    #        else:
    #            unique[u] = matching[u]



#print(bipartiteMatch(matching))
print(matching)

#print(unique)