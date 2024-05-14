#9. WAP to input the height of a person in inches and convert it to feet and inches.

height_inches = float(input("Enter the height of the person in inches: "))
height_feet = height_inches // 12
height_inches = height_inches % 12
print(f"The height of the person is {height_feet} feet and {height_inches} inches.")