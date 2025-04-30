"""Basic sorting example"""

fruits = ["pomegranate", "cherry", "apricot", "date", "Apple", "lemon", "Kiwi",
         "ORANGE", "lime", "Watermelon", "guava", "papaya", "FIG", "pear", "banana",
         "Tamarind", "persimmon", "elderberry", "peach", "BLUEberry", "lychee",
         "grape"]

sorted_fruit = sorted(fruits)  # sorted() returns a list

print(f"{sorted_fruit = }\n")

nums = [800, 80, 1000, 32, -3, 8, 18, 255, 400, 5, 5000]

print(f"{sorted(nums) = }")

sorted_fruit_ic = sorted(fruits, key=str.lower)
print(f"{sorted_fruit_ic = }\n")

def last_letter(s):
    sort_value = len(s)
    print(f"sorting {s} as {sort_value}")
    return sort_value

sorted_fruit_ll = sorted(fruits, key=last_letter)
print(f"{sorted_fruit_ll = }\n")


