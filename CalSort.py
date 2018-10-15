from bipartiteMatch import bipartiteMatch
#import numpy as np
import csv

data = {}

with open('SampleData.csv') as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',')

    for row in csv_reader:
        data[row[0]] = row[1:]

        matching = {'time':'name1' 'name2'}
        for u in data:
            for u2 in data:
                for v in data[u]:
                    for v2 in data[u2]:
                        if v not in matching and u != u2 and v == v2:
                            matching[v] = u, u2
                            break

        unique = {}
        for u in matching:
            if matching['tim' , 'name1' , 'name2'] in unique:
                break
            else:
                unique[u] = matching[u]



#print(bipartiteMatch(matching))
print(matching)

print(unique)