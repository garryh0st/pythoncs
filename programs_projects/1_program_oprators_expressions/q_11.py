#11. WAP to input the height and radius of a sphere and find its surface area and volume.

height = float(input("Enter the height of the sphere: "))
radius = float(input("Enter the radius of the sphere: "))
surface_area = 4 * 3.14 * radius**2
volume = 4/3 * 3.14 * radius**3
print(f"The surface area of the sphere is {surface_area} and the volume is {volume}.")