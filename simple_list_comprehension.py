colors = ['red', 'purple', 'yellow', 'black', 'pink']

c1 = []
for c in colors:
    item = c.upper()
    c1.append(item)
print(f"{c1 = }\n")

#    [ITEM for VAR in ITERABLE]
c2 = [c.upper() for c in colors]
print(f"{c2 = }\n")
