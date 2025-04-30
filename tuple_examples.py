
person = "Bill", "Gates", "Microsoft", "1955-10-28"
print(f"{person = }")
print(f"{type(person) = }")
print(f"{person[0] = }")
print(f"{person[-1] = }")
# person[0] = "William"  INVALID

# unpacking an iterable
first_name, last_name, product, dob = person
print(first_name, last_name)


