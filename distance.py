"""TW PROGRAM 1 """
"""Program to read distance in kilometers and then display it in meters(km*1000),
feets (1 meter = 3.2805399), inches (1 feet = 12 inches) and centimeters(1 inch = 2.56 cms)
"""
km = float(input("Enter the distance between two cities in kilometers: "))
meters = km * 1000
feets = meters * 3.2805399
inches = feets * 12
centimeters = inches * 2.56
print(km, f"Kilometers is ", meters, " in meters")
print(km, f"Kilometers is ", feets, " in feets")
print(km, f"Kilometers is ", inches, " in inches")
print(km, f"Kilometers is ", centimeters, " in centimeters")
