#1. Identify the correct and incorrect variable names:
#ii) fred
#iii) #sum total
#iv) xTwo
#v) if
#vi) Sumtotal
#vii) _static
#viii) 2x
#ix) While
#x) _4
#xi) 11. x2
#xii)sum_total
#xiii) sumTotal
#xiv) 10%
#xv) a27834
#xvi) sum-total

# Correct variable names: fred, xTwo, _static, _4, sum_total, sumTotal, a27834
# Incorrect variable names: #sum total, if, 2x, While, 11. x2, 10%, sum-total

#2. Assume the following declarations:
#f1 = 23.3; f2 = 1.0; d1 = 3.1; i1 = 5; i2 = 10; i3 = 7; s1 =11; s2 = 5; c1 = ‘0’;
#What is the result of the following expressions ? Express your answer as <value , type>. 
#a) fi + d1
#b) i1 + d1
#c) i1 + i2 * i3
#d) i2 % i3
#e) i3 / i2 + i1 * 15
#f) f1 – f2
#g) f1 – i3
#h) f1 / i2 + d1
#i) i2 + i3 + 3.0
#j) i2 * f2 + 4
#k) s1 / i3
#l) c1 + f2
#m) s1 + s2
#n) i3 + c1
#o) c1 – s2 

# a) 26.4, float
# b) 8.1, float
# c) 75, int
# d) 3, int
# e) 37.7, float
# f) 22.3, float
# g) 16.3, float
# h) 5.63, float
# i) 20.0, float
# j) 14.0, float
# k) 1.5714285714285714, float
# l) 1.0, float
# m) 16, int
# n) 7, int
# o) TypeError: unsupported operand type(s) for -: 'str' and 'int'


#3. output
#Give the output
#(i)
#a=2.30
#b=a+1
#print(a, b-a, sep=”\n”)
#(ii)
#Tree, guess, debt=4,3.9832,3.02
#print(”tree=”,Tree, sep=”\t”)
#print(”guess=”,guess, sep=”\n”)
#print(”debt=”, debt)

# (i)
# 2.3
# 1.0
# (ii)
# tree= 4
# guess=3.9832
# debt=3.02

#4. Underline the errors in the following. Also write the corrected code.
#(i) a=67
#b=input(“enter a number”)
#print(a+b)
#(ii) str1=”Good”
# str2=int(input(“Enter a number”))
# print(str1+str2)
#(iii) b=90
# print(“The values is”,B)
#(iv) x=y=90
# print(x+”y”)

# (i) a=67
# b=int(input(“enter a number”))
# print(a+b)
# (ii) str1=”Good”
# str2=str(input(“Enter a number”))
# print(str1+str2)
# (iii) b=90
# print(“The values is”,b)
# (iv) x=y=90
# print(x+y)

#5. Define the following
#a) An integer with the value 80.
#b) A fractional number with the value 42.11.
#c) A string with the constant “Hamburgers”
#d) A character with the value “A”

# a) 80
# b) 42.11
# c) "Hamburgers"
# d) 'A'

#6. Programming
#(i) WAP to declare a variable “Score” which can be used to store the runs made by a
#batsman. Accept the name and score of a batsman and display it with appropriate
#message.
#(ii) WAP to declare 3 variables p,r and t and assign values, 600, 4, 8.9 to them
#respectively. Also display the values along with variable names.
#(iii) WAP to input length and breadth of a rectangle and display area ans perimeter.
#(iv) WAP to input marks of a 4 student and display the average marks.In basic python

# (i)
name = input("Enter the name of the batsman: ")
score = int(input("Enter the score of the batsman: "))
print(f"{name} scored {score} runs.")

# (ii)
p = 600
r = 4
t = 8.9
print(f"p = {p}, r = {r}, t = {t}")

# (iii)
length = int(input("Enter the length of the rectangle: "))
breadth = int(input("Enter the breadth of the rectangle: "))
area = length * breadth
perimeter = 2 * (length + breadth)
print(f"Area: {area}, Perimeter: {perimeter}")

# (iv)
marks1 = int(input("Enter the marks of student 1: "))
marks2 = int(input("Enter the marks of student 2: "))
marks3 = int(input("Enter the marks of student 3: "))
marks4 = int(input("Enter the marks of student 4: "))
average = (marks1 + marks2 + marks3 + marks4) / 4
print(f"Average marks: {average}")


