import sys
import geometry
# find and load geometry.py

circle = geometry.circle_area(8)
print(f"{circle = }")

rectangle = geometry.rectangle_area(10, 12)
print(f"{rectangle = }")

square = geometry.square_area(7.9)
print(f"{square = }")

# module search rules
# 1. current folder
# 2. folders in PYTHONPATH
# 3. system folders  (sys.prefix/lib/....)

print('-' * 60)
for path in sys.path:
    print(path)
print()

print(f"{sys.prefix = }")
print(f"{sys.executable = }")
