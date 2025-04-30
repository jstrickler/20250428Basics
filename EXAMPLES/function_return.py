def get_hello():
    return "Hello, world"

h = get_hello() 
print(f"{h = }")

def hello():
    print("Hello, world")

h = hello()
print(f"{h = }")

def double(x):
    return x * 2

d = double(10)
print(f"{d = }")
print(f"{double('mint') = }")
print(f"{double(512.3903) = }")

m = "microphone"
print(f"{double(m) = }")
