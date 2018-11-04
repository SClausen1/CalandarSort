import csv
import pandas as pd

data = {}

df = pd.read_csv('SchedulingSpreadsheet.csv', usecols=lambda x: x in ['Please type your name.', 'Monday', 'Tuesday',
                                                                     'Wednesday', 'Thursday', 'Friday'])
df['Monday'] = df['Monday'].str.replace(' PM', 'M')
df['Monday'] = df['Monday'].str.replace(' AM', 'M')

df['Tuesday'] = df['Tuesday'].str.replace(' PM', 'T')
df['Tuesday'] = df['Tuesday'].str.replace(' AM', 'T')

df['Thursday'] = df['Thursday'].str.replace(' PM', 'Th')
df['Thursday'] = df['Thursday'].str.replace(' AM', 'Th')

df['Wednesday'] = df['Wednesday'].str.replace(' PM', 'W')
df['Wednesday'] = df['Wednesday'].str.replace(' AM', 'W')

df['Friday'] = df['Friday'].str.replace(' PM', 'F')
df['Friday'] = df['Friday'].str.replace(' AM', 'F')


csv_reader = df.to_csv()
print(csv_reader)
with open('SchedulingSpreadsheet.csv') as csv_file:
    csv_reader2 = csv.reader(csv_file, delimiter=',')

    for row in csv_reader:
        data[row[0]] = row[1:]

    # sort data by number of elements
    dataSort = {}
    for k in sorted(data, key=lambda k: len(data[k])):
        dataSort[k] = data[k]

    # iterate through the sorted data two names and two values at a time
    # once a match is found empty the values of that name
    matching = {}
    for name1 in dataSort:
        for name2 in dataSort:
            for v in dataSort[name1]:
                for v2 in dataSort[name2]:
                    if name1 != name2 and v == v2:
                        matching[v] = name1, name2
                        dataSort[name1] = ""
                        dataSort[name2] = ""
                        break
    # adds unmatched persons and all of their time slots to dict

    for name in dataSort:
        if dataSort[name] != "":
            matching[name] = dataSort[name]


print(matching)


