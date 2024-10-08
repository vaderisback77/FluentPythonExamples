my_cars = [
    ("SUV", "Land Rover Evoque", 2013),
    ("Sedan", "Tesla Model Y", 2020),
    ("Motorcyle", "Suzuki GSXR600", 2014),
]
## If I want to print all fields in the tuple
for type, name, year in my_cars:
    print(f"vehicle type: {type}, vehicle name: {name}, year of build: {year}")

## If I only want to print a subset of the fields in the tuple

for type, name, _ in my_cars:
    print(f"vehicle type: {type}, vehicle name: {name}")

## what if I want to print only field from the tuple

for type, name, year in my_cars:
    if type == "SUV":
        print(f"vehicle name: {name}, vehicle year: {year}")

"""
Output:
vehicle type: SUV, vehicle name: Land Rover Evoque, year of build: 2013
vehicle type: Sedan, vehicle name: Tesla Model Y, year of build: 2020
vehicle type: Motorcyle, vehicle name: Suzuki GSXR600, year of build: 2014
vehicle type: SUV, vehicle name: Land Rover Evoque
vehicle type: Sedan, vehicle name: Tesla Model Y
vehicle type: Motorcyle, vehicle name: Suzuki GSXR600
vehicle name: Land Rover Evoque, vehicle year: 2013
%
"""
