import csv

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


