import math

# Constants
density_of_water = 1000  # in kg/m^3

# Inputs
diameter_cm = float(input("Enter the diameter of the jet in cm: "))
velocity_jet = float(input("Enter the velocity of the jet in m/s: "))
velocity_plate = float(input("Enter the velocity of the plate in m/s: "))

# Converting diameter to meters
diameter_m = diameter_cm / 100

# Calculating area of the jet (in m^2)
area = (math.pi / 4) * (diameter_m ** 2)

# Calculating relative velocity (v - u)
relative_velocity = velocity_jet - velocity_plate

# Calculating force exerted by the jet on the plate
force = density_of_water * area * (relative_velocity ** 2)

# Calculating work done per second by the jet on the plate
work_done = force * velocity_plate

# Output
print(f"The force exerted by the jet on the plate is: {force:.2f} N")
print(f"The work done by the jet on the plate per second is: {work_done:.2f} W")
