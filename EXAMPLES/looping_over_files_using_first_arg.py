import sys

search_term = sys.argv.pop(1)  # gets the 1st non-script-name arg

print(f"search term is '{search_term}'")
for file_path in sys.argv[1:]:  # skip script name
    print(f"Processing {file_path}")
    with open(file_path) as file_in:
        for raw_line in file_in:
            if search_term in raw_line:
                line = raw_line.rstrip()
                print(line)

