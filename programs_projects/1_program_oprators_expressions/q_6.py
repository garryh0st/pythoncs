#6. WAP to input the marks of a student in five subjects and calculate total marks and percentage.
subject_1 = float(input("Enter the marks of subject 1: "))
subject_2 = float(input("Enter the marks of subject 2: "))
subject_3 = float(input("Enter the marks of subject 3: "))
subject_4 = float(input("Enter the marks of subject 4: "))
subject_5 = float(input("Enter the marks of subject 5: "))
total_marks = subject_1 + subject_2 + subject_3 + subject_4 + subject_5
percentage = total_marks / 500 * 100
print(f"The total marks of the student is {total_marks} and the percentage is {percentage}.")   
# Output: Enter the marks of subject 1: 50
# Enter the marks of subject 2: 60
# Enter the marks of subject 3: 70
# Enter the marks of subject 4: 80
# Enter the marks of subject 5: 90
# The total marks of the student is 350.0 and the percentage is 70.0.