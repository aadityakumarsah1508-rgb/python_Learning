# Question 38:- Math > Find angle MBC

# approach:- 
# by pythagores theorem, sq(AC) = sq(AB) + sq(AC) 
# MC = AC/2; 
# Now we know the value of BC and MC, also tr(MCB) is iso. so 
# <m + <C + <B = 180 
# <B == <C so, 2<B + <M = 180 
# this approach not worked

import math

ab = float(input())
bc = float(input())

#learning Python
# angle = math.radians(ab//bc)
# # angle = math.tan(angle_rad)
# does not workk 

# Solution from AI
angle_rad = math.atan2(ab, bc)
angle_deg = math.degrees(angle_rad)
angle = int(angle_deg)
# print(round(angle,"\u00b0"))
print(f"{angle}\u00b0")