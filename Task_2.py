import math
n = int(input("Enter a number: "))
a = n ** (1/2)
print("Square Root: ",a)

if n > 0:
    b = math.log(n)
else:
    b = "undefined"
print("Logarithm: ", b)

c = math.sin(n)
print("Sine: ", c)