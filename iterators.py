colors = ["red", "blue", "green", "yellow", "brown", "black"]

rev_colors = reversed(colors)
print(f"{rev_colors = }")

for color in rev_colors:
    print(color)
print('-' * 60)

for i, color in enumerate(colors):
    print(i, color)
print()
things = ["baron", "lagoon", "giant", "bird", "tree", "licorice"]
combos = zip(colors, things)
print(f"{combos = }")
for color, thing in combos:
    print(color, thing)
print()

combos = zip(colors, things)
print(f"{list(combos) = }")
print()
for i in range(5):
    print("Are we having fun yet?")
print("   -- YES!")

# range(stop-before)
# range(start-at, stop-before)
# range(start-at, stop-before, count-by)
for i in range(1, 11):
    print(i)
print()

