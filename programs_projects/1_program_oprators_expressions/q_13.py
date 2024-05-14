#13. WAP to find the roots of a quadratic equation. Input the value of a, b and c. with basic python operators.


a = float(input("Enter the value of a: "))
b = float(input("Enter the value of b: "))
c = float(input("Enter the value of c: "))
d = b**2 - 4*a*c
root1 = (-b + d**0.5) / 2*a
root2 = (-b - d**0.5) / 2*a
print(f"The roots of the quadratic equation are {root1} and {root2}.")