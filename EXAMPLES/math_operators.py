a = 23
b = 7

print(a + b, a - b, a * b)  # normal operations

print(a / b, a // b, a / -b, a // -b)   # division and floored division
  
print(a ** b)   # exponentiation   # a ** .5  square root

print(a % b)   # modulus (remainder)

x = 22
x += 10  # Same as x = x + 10
print(f"{x = }")
print()

# P E MD AS
alpha = 1
beta = 2
gamma = 3
delta = 4
print(f"{alpha + beta * gamma / delta = }")
print(f"{(alpha + beta) * (gamma / delta) = }")
print(f"{(alpha + (beta * gamma)) / delta = }")
print(f"{alpha + ((beta * gamma) / delta) = }")

