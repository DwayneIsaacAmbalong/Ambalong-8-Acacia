import math

x1 = int(input("What is the x1? "))
x2 = int(input("What is the x2? "))
y1 = int(input("What is the y1? "))
y2 = int(input("What is the y2? "))

x3 = x2 - x1
y3 = y2 - y1

x = pow(x3,2)
y = pow(y3,2)

d1 = x + y
d = (math.sqrt(d1))
print("The distance between the two points is: ",d, )

#Reflection
# I learned how to use libraries and other function and also I learned proper variable placement or else it will be wrong.
# Libraries are also very practical rather than making the raw code from scratch.
# So basically libraries made our coding lives easier.