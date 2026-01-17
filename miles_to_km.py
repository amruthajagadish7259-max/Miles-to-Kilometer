import sys

if len(sys.argv) > 2:
    miles = float(sys.argv[1])
else:
    miles = 4

result = miles * 1.609
print("Miles to kilometer converted value is:", result)
