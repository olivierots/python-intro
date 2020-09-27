# Data Types: numbers
# create a program to calculate the area & circumference of a circle
# ask the user for the radius
# area = π x r^2
# circumference = 2 x π x r
# C	=	circumference
# π	=	the constant pi
# r	=	radius of the circle

import math
radius = float ( input("type the radius of the circle: " ) )
area = math.pi * ( radius ** 2 )
circumference = 2 * math.pi * radius

# the round module round the result to two decimal places
print ("The area of the circle is", round(area,2))
print ("The circumference of the circle is", round(circumference,2))
                       
