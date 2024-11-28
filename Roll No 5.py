import math

# Constants
density_of_water = 1000  # in kg/m^3
velocity_coefficient = 0.95  # Coefficient of velocity
g = 9.81  # Acceleration due to gravity in m/s^2

# Inputs
diameter_cm = float(input("Enter the diameter of the nozzle in cm: "))
head_of_water = float(input("Enter the head of water in meters: "))

# Converting diameter to meters
diameter_m = diameter_cm / 100

# Calculating area of nozzle (in m^2)
area = (math.pi / 4) * (diameter_m ** 2)

# Calculating theoretical velocity (Vth)
Vth = math.sqrt(2 * g * head_of_water)

# Calculating actual velocity (V)
V = velocity_coefficient * Vth

# Calculating force exerted (F)
force = density_of_water * area * (V ** 2)

# Output
print(f"The force exerted by the jet of water on the fixed vertical plate is: {force:.2f} N")
