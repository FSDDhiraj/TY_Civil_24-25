import math

# Constants
density_of_water = 1000  # in kg/m^3

# Inputs
diameter_cm = float(input("Enter the diameter of the jet in cm: "))
velocity = float(input("Enter the velocity of the jet in m/s: "))

# Convert diameter from cm to meters
diameter_m = diameter_cm / 100

# Calculate the area of the jet (  in m^2)
area = (math.pi / 4) * (diameter_m ** 2)

# Calculate the force exerted by the jet on the plate
force = density_of_water * area * (velocity ** 2)

# Output
print(f"The force exerted by the jet on the stationary plate is: {force:.2f} N")
