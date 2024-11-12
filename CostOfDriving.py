"""Cost of driving"""
distance = float(input("Enter the distance in miles \n"))
milesPerGallon=float(input("Enter miles per gallon \n"))
totalNumberOfMiles=distance/milesPerGallon
price=float(input("Price of fuel for each gallon \n "))
print("The cost of driving is ", totalNumberOfMiles*price)
