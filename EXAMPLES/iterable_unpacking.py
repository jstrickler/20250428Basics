values = ['a', 'b', 'c']

x, y, z = values  # unpack values (which is an iterable) into individual variables

print(x, y, z)
print()

people = [
    ('Bill', 'Gates', 'Microsoft'),
    ('Steve', 'Jobs', 'Apple'),
    ('Paul', 'Allen', 'Microsoft'),
    ('Larry', 'Ellison', 'Oracle'),
    ('Mark', 'Zuckerberg', 'Facebook'),
    ('Sergey', 'Brin', 'Google'),
    ('Larry', 'Page', 'Google'),
    ('Linux', 'Torvalds', 'Linux'),
]
print(f"{type(people) = }")
print(f"{type(people[0]) = }")
print(f"{people[0] = }")
print(f"{people[0][0] = }")


for row in people:
    first_name, last_name, _ = row  # unpack row into variables
    print(first_name, last_name)
print()

# for VAR(s) in ITERABLE:
#   ...
for first_name, last_name, _ in people:  # a for loop unpacks if there is more than one variable
    print(first_name, last_name.upper())
print()

for person in people:
    if 'Larry' in person:
        print(person)
print()