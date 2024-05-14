#5. WAP to input the length and breadth of a rectangle and calculate the area and circumference.

length = float(input("Enter the length of the rectangle: "))
breadth = float(input("Enter the breadth of the rectangle: "))
area = length * breadth
circumference = 2 * (length + breadth)
print(f"The area of the rectangle is {area} and the circumference is {circumference}.")
# Output: Enter the length of the rectangle: 5
# Enter the breadth of the rectangle: 10
# The area of the rectangle is 50.0 and the circumference is 30.0.
