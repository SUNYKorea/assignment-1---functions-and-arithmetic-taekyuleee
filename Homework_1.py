# Name: Taekyu Lee
# SBUID: 114946466

# Remove the ellipses (...) when writing your solutions.

# ---------------------------- Exercise I ---------------------------------------
# ----------------- Convert Fahrenheit to Celsius -------------------------------
# TODO: Complete the implementation of fahrenheit2celsius () and what_to_wear(). 

def fahrenheit2celsius(fahrenheit): 
   celsius = 5/9 *(fahrenheit-32)
   return celsius
def what_to_wear(celsius):
   if celsius < -10:
       return "Wear a puffy jacket"
   elif -10 <= celsius < 0:
       return "Wear a scarf"
   elif 0 <= celsius < 10:
       return "Wear a sweater"
   elif 10 <= celsius < 20:
       return "Wear a light jacket"
   else:
       return "Wear a T-shirt"
   # ---------------------------- Exercise II --------------------------------------
# ----------------- Area and perimeter of a triangle  ---------------------------
# TODO: Fill the functions shoelace_triangle_area, euclidean_distance and
# compute_triangle_perimeter from scratch  

def shoelace_triangle_area(x1, y1, x2, y2, x3, y3):
    area = abs((x1*y2+x2*y3+x3*y1) - (x1*y3+x2*y1+x3*y2)) / 2
    return area

def euclidean_distance(x1, y1, x2, y2):
    distance= ((x1-x2)**2 + (y2-y1)**2)
    return distance

def compute_triangle_perimeter(x1, y1, x2, y2, x3, y3):
    side1=euclidean_distance(x1,y1,x2,y2)
    side2=euclidean_distance(x2,y2,x3,y3)
    side3=euclidean_distance(x3,y3,x1,y1)
    perimeter= side1+side2+side3
    return perimeter
# ---------------------------- Exercise III -------------------------------------
# ----------------- Compute the area of a regular polygon -----------------------
# TODO: Fill the functions deg2rad, apothem  and polygon_area 


def deg2rad(deg):
    return math.p1*deg/180

def apothem(number_sides, length_side):
    return number_sides/(2*math.tan(math.pi/length_side))

def polygon_area(number_sides, length_side):
    a=apothem(number_sides)*(length_side)
    perimeter=number_sides*length_side
    return 0.5*a*perimeter

# ---------------------------- Test -------------------------------------
# The following lines are for testing purposes, and will not be part of
# your grade. You may freely modify the following codes.

# Exercise 1 test
#fahrenheit = 40
#what_to_wear(fahrenheit2celsius(fahrenheit))

temperature = -10
what_to_wear(temperature)

'''
# Exercise 2 test 
x1, x2, x3, y1, y2, y3 = -4, -5, 3, -4, 5, -3 # declaration of the vertices of the triangle
area = shoelace_triangle_area(x1, y1, x2, y2, x3, y3)
perimeter = compute_triangle_perimeter(x1, y1, x2, y2, x3, y3)
print("The area of the triangle is : " + str(area) + " , its perimeter is : " + str(perimeter) )

# Exercise 3 test
number_sides = 5
length_side = 4
print ("The area of the polygon is : " + str(polygon_area(number_sides, length_side)))
'''

