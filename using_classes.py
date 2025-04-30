names = list()
names = [] # names is an 'instance' of the 'list' class 

names.append("Chelsea")
names.append("John")
names.append("Anupam")

print(f"{names = }")
names.insert(0, "Nellie")
names.insert(2, "Clare")
print(f"{names = }")

print(f"{len(names) = }")
print(f"{names[0] = }")

class Dog:
    def bark(self):
        print("Woof! woof")

d1 = Dog()
d2 = Dog()
d3 = Dog()

d1.bark()
d3.bark()
