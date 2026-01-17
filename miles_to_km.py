import sys
if sys.argv:
    miles=float(input("Enter distance in miles:"))
else:
    miles=4

result=miles*1.607
print("Miles to kilometer converted value is:",result)
