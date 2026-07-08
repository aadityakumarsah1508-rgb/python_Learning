# question 31: Math > Polar Coordinates

import cmath

# Read the complex number input from STDIN
z = complex(input().strip())

# Calculate the modulus (r) and phase (phi)
r = abs(z)
phi = cmath.phase(z)

# Print the results
print(r)
print(phi)