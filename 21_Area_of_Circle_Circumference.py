''' Area of Circle and Circumference
Formula:
Area = pi * r ** 2
Circumference= 2 * pi * r
'''
import math as m
r=float(input('Enter the Radius:'))
a=m.pi * r ** 2
c=2 * m.pi * r
print("The Area of the Circle is %.2f and Circumference is %.2f"%(a,c))
