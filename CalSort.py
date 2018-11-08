import csv
import pandas as pd

# Calander Sorting Algorithm
# Steven Clausen
data = {}

df = pd.read_csv('SchedulingSpreadsheet.csv', usecols=lambda x: x in ['Please type your name.', 'Monday', 'Tuesday',
                                                                     'Wednesday', 'Thursday', 'Friday'])

days = ['Monday', 'Tuesday','Wednesday', 'Thursday', 'Friday']

# THIS IS TO OUTPUT ALL POSSIBLE TIME SLOTS --> Copy output into ALLDAYS array
# for ind, person in df.iterrows():
#     i = 0
#     alldays = []
#     for day in person:
#         if i==0:
#             name = day
#         else:
#             if not str(day)=='nan':
#                 splt = day.split(',')
#                 splt = [days[i-1][0:2] + item.strip() for item in splt]
#                 alldays = alldays + splt
#         i += 1
#
#     data[name] = alldays
#
# print(data['NoFace'])
# exit()

ALLDAYS = ['Mo9-10 AM', 'Mo12-1 PM', 'Mo5-6 PM', 'Tu11-12 PM', 'Tu2-3 PM', 'Tu3-4 PM', 'Tu4-5 PM', 'Tu5-6 PM', 'Tu7-8 PM', 'We10-11 AM', 'We11-12 PM', 'We12-1 PM', 'We1-2 PM', 'We2-3 PM', 'We3-4 PM', 'We4-5 PM', 'We5-6 PM', 'We7-8 PM', 'We8-9 PM', 'We9-10 PM', 'Th11-12 PM', 'Th2-3 PM', 'Th3-4 PM', 'Th4-5 PM', 'Th5-6 PM', 'Th7-8 PM', 'Fr9-10 AM', 'Fr10-11 AM', 'Fr11-12 PM', 'Fr12-1 PM', 'Fr1-2 PM', 'Fr2-3 PM', 'Fr3-4 PM', 'Fr4-5 PM', 'Fr5-6 PM', 'Fr7-8 PM']

data = {}
for ind, person in df.iterrows():
    i = 0
    alldays = []
    for day in person:
        if i==0:
            name = day
        else:
            if not str(day)=='nan':
                splt = day.split(',')
                splt = [ALLDAYS.index(days[i-1][0:2] + item.strip()) for item in splt]
                alldays = alldays + splt
        i += 1

    data[name] = alldays
# print(data)
# exit()


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
for i in range(1, 6):
    filename = 'SampleData' + str(i) + '.csv'
    print ('*** Worksing on ', filename,  '----------------------')

    data = {}

    with open(filename) as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=',')

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


