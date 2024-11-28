import math

# Constants
side_slope_n = 0.5  # 1 horizontal and 2 vertical, so n = 1/2 = 0.5
bed_slope = 1 / 1500
chezy_constant = 50

# Inputs
area = float(input("Enter the area of cross section in m^2: "))

# Finding depth of flow (d) for the most economical section
# m = d / 2, and A = (b + nd)d

# Step 1: Assuming that depth d is half of the hydraulic radius (R = A / P for most economical section)
# Solving for d iteratively
d = math.sqrt(area / (1 + side_slope_n))  # Initial guess for d

# Calculate the base width (b) for the most economical section
b = (area / d) - (side_slope_n * d)

# Calculate the wetted perimeter P
wetted_perimeter = b + 2 * d * math.sqrt(side_slope_n**2 + 1)

# Calculate hydraulic radius m
hydraulic_radius = area / wetted_perimeter

# Calculate discharge Q
discharge = area * chezy_constant * math.sqrt(hydraulic_radius * bed_slope)

# Output
print(f"The depth of flow (d) for the most economical section is: {d:.2f} m")
print(f"The base width (b) for the most economical section is: {b:.2f} m")
print(f"The discharge (Q) is: {discharge:.2f} m^3/sec")
