import csv

with open('misc/names.csv') as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',')
    line_count = 0
    class_roster = []
    for row in csv_reader:
        if line_count == 0:
            line_count += 1
        else:
            name = "{} {}".format(row[0], row[1])
            class_roster.append(name)
            line_count += 1
    # print(f'Processed {line_count} lines.')

# print(class_roster)
