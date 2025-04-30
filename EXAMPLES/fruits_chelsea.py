
fruit_list = []

with open('../DATA/fruit.txt') as fruit_in:
    for raw_line in fruit_in:
        fruit_list.append(raw_line.rstrip())

print(f"{fruit_list = }")
