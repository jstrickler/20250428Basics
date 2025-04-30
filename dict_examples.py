d1 = {}   # new, empty dictionary
d2 = dict()  # same same

state_capitals = {}
state_capitals['NC'] = "Raleigh"
state_capitals['CA'] = "Sacramento"
state_capitals['FL'] = "Tallahassee"
print(f"{state_capitals = }\n")

print(f"{state_capitals['NC'] = }")

grades = {'Abdul': 'A', 'Betty': 'B', 'Connie': 'C', 'Edgar': 'B'}
print(f"{grades['Connie'] = }")

grades['Connie'] = 'F'
grades['John'] = 'D'
grades['Seth'] = 'A-'
print(f"{grades = }\n")

#  DICT[KEY]
# print(f"{grades['Tom'] = }")
print(f"{grades.get('Tom') = }")
print(f"{grades.get('Tom', 0) = }")
print(f"{grades.get('Connie') = }")

print(f"{grades.setdefault('Tom', 'B') = }")
print()
print(f"{grades = }\n")

for k in 'Tom', 'Randy', 'Maribel', 'Seth':
    print(k, k in grades)
print()

for name, grade in grades.items():
    print(name, grade)
print()
print(f"{grades.items() = }")
print(f"{grades.values() = }")
print(f"{grades.keys() = }")
print()

for name, grade in sorted(grades.items()):
    print(name, grade)



