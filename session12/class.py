import random

class_roster = {'Jonathan Beltran': 0, 'Allison Fernandez': 1, 'Siddhanth Goyal': 0, 'Jingyu He': 0, 'Defne Ikiz': 0, 'Zirui Jiao': 0, 'Pranjal Joshi': 0, 'Dong Hyun Kim': 0, 'Ha Min Ko': 0, 'Kyle Lawson': 0, 'Christine Lee': 1, 'Connie Li': 1,
               'Qinyi Li': 0, 'Matthew Michalke': 0, 'Ho Wang Alastair Ng': 1, 'Jonghyun Park': 0, 'Alden Pexton': 2, 'Shriya Rathi': 2, 'Waylon Ryan': 1, 'Christian Thompson': 3, 'Angela Tsung': 2, 'Aaron Wendell': 0, 'Sarah Zazyczny': 0, 'Shiyue (Shirley) Zong': 0}

min_times = min(class_roster.values())

print(min_times)

pool = []

for name in class_roster:
    if class_roster[name] == min_times:
        pool.append(name)
    
random_name = random.choice(pool)

print(random_name)
print(class_roster[random_name])
class_roster[random_name] += 1
print(class_roster[random_name])