# Question 25:- Strings > Alphabet Rangoli

# Approaching the question
size = 3
char_no = 96 + int(3)
# print(chr(char_no))

# Trying to print things in for loop

# for i in range(97, char_no + 1):
#     print(chr(i))

# Trying to solve problem with hard code.

start = 97 
end = 96 + 3
direction = -1
# print(end)
while end != 96:
    print(end)
    end -= direction
    if end == 97:
        end += end