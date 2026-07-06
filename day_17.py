# # # Question :- Previous unsolved question 
# n = int(input())

# # # rows = 2n - 1
# # # columns = 4n -3
# # # checking the working of chr func.
# # print(chr(96+n))

# # # for i in range(97, 97+n):
# # #     print(chr(i))

# # # for i in range(96+n, 96, -1):
# # #     print(chr(i), end="")


# ch = []
# start = 96+n
# for i in range(start, 96, -1):
#     ch.append(i)

# for i in range(98, 97+n):
#     ch.append(i)

# for i in ch:
#     print(chr(i), end="") 
#     # print(chr(i), end="-") 

# # # Another method
# # for i in range(2*n+1):
# #     print(i, end="")

# for i in range(1,2*n):
#     for j in range(1, 4*n-2):
#         # print(j, end="")
#         pass
#     print("")

# ================================================================================================

# Solution of the alphabet rangoli question

def print_rangoli(size):
    import string
    # Get all lowercase letters
    alphabets = string.ascii_lowercase
    
    # Slice the alphabets we need for this size (e.g., 'a' to 'e' for size 5)
    letters = alphabets[:size]
    
    lines = []
    
    # Generate the top half and middle line
    for i in range(size):
        # Grab the letters needed for the current row, moving inward
        # For size 5, row 0 needs 'e', row 1 needs 'e-d', etc.
        row_letters = letters[size - i - 1 : size]
        
        # Reverse them to go down to the lowest letter, then add the mirror ascending back up
        # e.g., 'e-d' becomes 'e-d' + 'e' -> 'e-d-e'
        full_row = row_letters[::-1] + row_letters[1:]
        
        # Join with hyphens
        row_str = "-".join(full_row)
        
        # Center the row to the total width of the center-most line
        total_width = 4 * size - 3
        lines.append(row_str.center(total_width, "-"))
        
    # Combine the top half (excluding the center line) in reverse to make the bottom half
    # then print everything separated by a newline
    final_rangoli = lines + lines[:-1][::-1]
    print("\n".join(final_rangoli))

if __name__ == '__main__':
    n = int(input())
    print_rangoli(n)
