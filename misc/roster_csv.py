import random
import csv
from pprint import pprint


def call(filename):
    '''
    Among the names that are called least times,
    return one name randomly. Update database after each call.

    filename: the name of csv file

    returns one name
    '''
    roster = display_all(filename)
    visits_list = []
    for student in roster:
        visits_list.append(roster[student])
    min_visits = min(visits_list)

    # create a list, names, to store the least called names
    names = []
    for student in roster:
        if roster[student] == min_visits:
            names.append(student)
    # or
    # names = [name for name in roster.keys() if roster[name]==min_visits]

    name_to_update = random.choice(names)
    roster[name_to_update] += 1

    with open(filename, mode='w', newline='') as fp:
        writer = csv.writer(fp)
        for name, number in roster.items():
            writer.writerow([name, number])

    return name_to_update


def display_all(filename):
    '''
    return a dict of all names and values

    filename: the name of csv file
    '''
    with open(filename, mode='r') as fp:
        reader = csv.reader(fp)
        roster = {row[0]: int(row[1]) for row in reader}
    return roster


def main():
    ROSTER_FILE = 'misc/roster.csv'
    # pprint(display_all(ROSTER_FILE))
    print(call(ROSTER_FILE))
    # pprint(display_all(ROSTER_FILE))


if __name__ == '__main__':
    main()
