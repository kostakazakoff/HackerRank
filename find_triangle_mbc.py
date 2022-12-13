from math import sqrt, degrees, acos


a, b = int(input()), int(input())
c = sqrt(a*a + b*b)
angle = acos(b/c)

print(f'{round(degrees(angle))}{chr(176)}')
