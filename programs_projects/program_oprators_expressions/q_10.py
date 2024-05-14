#10. WAP to input the distance between two places in meters and convert it into kilometers and meters.

distance_meters = float(input("Enter the distance between two places in meters: "))
distance_kilometers = distance_meters // 1000
distance_meters = distance_meters % 1000
print(f"The distance between two places is {distance_kilometers} kilometers and {distance_meters} meters.")