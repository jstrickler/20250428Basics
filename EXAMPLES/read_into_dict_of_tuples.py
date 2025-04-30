from pprint import pprint

knight_info = {}  # create empty dict

with open("../DATA/knights.txt") as knights_in:
    for line in knights_in:
        name, title, color, quest, comment = line.rstrip('\n\r').split(":")
        knight_info[name] = title, color, quest, comment  # create new dict element with name as key and a tuple of the other fields as the value

pprint(knight_info, sort_dicts=True)
print()

#    KEY, VALUE in DICT.items()
for name, info in knight_info.items():
    print(f"{name = }")
    print(f"{info = }")
    print(info[0], name)
    print('-' * 5)    

print()
print(knight_info['Robin'], "\n")
print(knight_info['Robin'][2])
