import math
a = float(input("Enter 1st sides of triangle "))
b = float(input("Enter 2nd sides of triangle "))
c = float(input("Enter 3rd sides of triangle "))
s = a/2+b/2+c/2
p = s-a
q = s-b
r = s-c
z = p*q*r
print("The area of the given triangle is " , math.sqrt(s*z))
