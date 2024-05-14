#1. List the various types of mathametical operators in Python.

# +, -, *, /, %, **, //


#2. Construct logical expressions for the following situations in python:
#(a) Age is between 90 and 99
#(b) Department is ‘s’ and salary is more than 15000
#(c) ch is a vowel
#(d) Either roll no is even or marks are more than 90
#(e) Cost price is more than selling price and selling price is more than 600
#(f) ans is either ‘y’ ,’n’,’Y’ or ‘N’ 

# (a) 90 <= age <= 99
# (b) department == 's' and salary > 15000
# (c) ch in 'aeiou'
# (d) roll_no % 2 == 0 or marks > 90
#(e) cost_price > selling_price and selling_price > 600
# (f) ans in ['y', 'n', 'Y', 'N']

#3. Write equivalent Python statements for the following:
#(a) b^2 +4ac
#(b) –(a^2-b^2)
#(c) a+b/c+d
#(d) a(b/c)
#(e) 1/1+x2
#(f) (a+b)(c+d)(e+f)

# (a) b**2 + 4*a*c
# (b) -(a**2 - b**2)
# (c) a + b / c + d
# (d) a * (b / c)
# (e) 1 / (1 + x**2)
# (f) (a + b) * (c + d) * (e + f)



#4. Find out the errors in the following code fragments:
#(a) payrate=6.50; old salary=payrate*40;
# new salary= payrate*90;
#(b) abc,xyz=9,2
#print(ABC, XYZ)
#
#(c) w=a/b;
#print(w)
#(d) xyz=’A’
#print(xyz+2)

# (a) 
payrate = 6.50
old_salary = payrate * 40
new_salary = payrate * 90
print(new_salary)

# (b)
abc, xyz = 9, 2
print(abc, xyz)

# (c)
a = 10
b = 2
w = a / b
print(w)

# (d)
xyz = 'A'
print(xyz + '2')

#5) Write a program that computes the volume of an object . The program should ask the
#user to input the object’s mass and density . The mass will be given in grams ; the
#density will be in grams per cubic centimeter . The relationship of mass , density ,
#and volume of an object is given by :
# DENSITY = MASS / VOLUME
# Your program should output the volume in cubic centimeter

mass = float(input("Enter the mass of the object in grams: "))
density = float(input("Enter the density of the object in grams per cubic centimeter: "))
volume = mass / density
print(f"The volume of the object is {volume} cubic centimeters.")



#6) What is the result of the expression ? Express your answer as <value,type>.
#a) 25 / 7
#b) 21 / 3
#c) 14 % 3
#d) 31 % 3
#e) 22.1 + 1.0
#f) 7 – 21
#g) 28 + 3 * 5
#h) ( 27 / 3 ) + 15
#i) 2
#j) –23 + 7 * 2 

# (a) name = 3.5714285714285716, float
# (b) name = 7.0, float
# (c) name = 2, int
# (d) name = 1, int
# (e) name = 23.1, float
# (f) name = -14, int
# (g) name = 43, int
# (h) name = 24.0, float
# (i) name = 2, int
# (j) name = -9, int


#(8) Which library should be imported for the following functions?
#(a) pow()
#(b) sqrt() 

# (a) math
# (b) math

#(9) WAP to input the radius of a circle and display circumference and area with basic python operators.

radius = float(input("Enter the radius of the circle: "))
circumference = 2 * 3.14 * radius
area = 3.14 * radius**2
print(f"The circumference of the circle is {circumference} and the area of the circle is {area}.")

#(10) WAP to input the principal, rate a nd time and display the simple Interest.

principal = float(input("Enter the principal amount: "))
rate = float(input("Enter the rate of interest: "))
time = float(input("Enter the time period: "))
simple_interest = (principal * rate * time) / 100
print(f"The simple interest is {simple_interest}.")

#(11) WAP to input the name of a student and marks in 4 subjects. Diaply the toatl and
#percentage along with the name.

name = input("Enter the name of the student: ")
marks1 = float(input("Enter the marks in subject 1: "))
marks2 = float(input("Enter the marks in subject 2: "))
marks3 = float(input("Enter the marks in subject 3: "))
marks4 = float(input("Enter the marks in subject 4: "))
total_marks = marks1 + marks2 + marks3 + marks4
percentage = (total_marks / 400) * 100
print(f"The total marks of {name} is {total_marks} and the percentage is {percentage}.")





