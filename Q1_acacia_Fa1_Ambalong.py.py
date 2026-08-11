import math

x1 = int ( input ( "What is the x1? " ) )
x2 = int ( input ( "What is the x2? " ) )
y1 = int ( input ( "What is the y1? " ) )
y2 = int ( input ( "What is the y2? " ) )
#The codes on top of this comment are the questions that will ask the inputs your are going to put

x3 = x2 - x1
y3 = y2 - y1
#This is the first step in solving the distance of the 2 points

x = pow (x3 , 2 )
y = pow (y3 , 2 )
#This is the 2nd step in solving the distance of the 2 points

d1 = x + y
d = ( math.sqrt ( d1 ) )
#this is the final step

print ( "The distance between the two points is: " ,d, )
#this code will print the output

#Reflection
# I learned how to use libraries and other function and also I learned proper variable placement or else it will be wrong.
# Libraries are also very practical rather than making the raw code from scratch.
# So basically libraries made our coding lives easier.
