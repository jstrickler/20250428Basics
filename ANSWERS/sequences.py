ctemps = [-40.0, 0.0, 37.0, 75.0, 100.0]

for c in ctemps:
    f = ((9 * c) / 5) + 32
    print(f"{c:6.1f} C is {f:6.1f} F")

print()

fruits = [
    '    MANGO', 'Apple', '   peach   ', 'PLUM   ', '  Apricot',
    'BaNaNa', 'Persimmon   '
]

clean_fruits = [f.strip().lower() for f in fruits]

print(clean_fruits)
