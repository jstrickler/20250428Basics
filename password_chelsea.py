FILE_PATH = "DATA/passwd"

# sync:x:5:0:sync:/sbin:/bin/sync

def main():
    counts = get_counts()
    display_counts(counts)

def get_counts():
    shell_count = {}

    with open(FILE_PATH) as passwd_in:  # open file for reading
        # iterate over lines in file (line retains \n)
        for raw_line in passwd_in:
            line = raw_line.strip().split(":")
            # print(line)
            shell = line[6]
            if shell == "":
                shell = "NONE"

            if shell in shell_count:
                current_value = shell_count[shell]
                new_value = current_value + 1
                shell_count[shell] = new_value 
            else:
                shell_count[shell] = 1  # new element in dict

    return shell_count

def display_counts(counts_dict):    
    for shell, count in sorted(counts_dict.items()):
        print(f"{shell:15s} {count:3d}")

main()