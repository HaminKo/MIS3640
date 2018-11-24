import random

class_roster = {'Aaron Wendell': 0,
                'Alden Pexton': 2,
                'Allison Fernandez': 1,
                'Angela Tsung': 2,
                'Christian Thompson': 3,
                'Christine Lee': 1,
                'Connie Li': 1,
                'Defne Ikiz': 0,
                'Dong Hyun Kim': 0,
                'Ha Min Ko': 0,
                'Ho Wang Alastair Ng': 1,
                'Jingyu He': 0,
                'Jonathan Beltran': 0,
                'Jonghyun Park': 0,
                'Kyle Lawson': 0,
                'Matthew Michalke': 0,
                'Pranjal Joshi': 0,
                'Qinyi Li': 0,
                'Sarah Zazyczny': 0,
                'Shiyue (Shirley) Zong': 0,
                'Shriya Rathi': 2,
                'Siddhanth Goyal': 0,
                'Waylon Ryan': 1,
                'Zirui Jiao': 0}

min_times = min(class_roster.values())

print(min_times)

pool = []

for name in class_roster:
    if class_roster[name] == min_times:
        pool.append(name)


random_name = random.choice(pool)

print(random_name)
class_roster[random_name] += 1

# TODO: store the data
