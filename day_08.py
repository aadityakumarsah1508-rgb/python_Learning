# Question 16:- What's Your Name

def print_full_name(first, last):
    # Write your code here
    # full_name = first + last
    # return full_name
    print(f"Hello {first} {last}! You just delved into python.")

if __name__ == '__main__':
    first_name = input()
    last_name = input()
    print_full_name(first_name, last_name)

# ===============================================================================================

# Question 17:- Mutation

def mutate_string(string, position, character):
    l = list(string)
    l[position] = character
    string = ''.join(l)
    return string

if __name__ == '__main__':
    s = input()
    i, c = input().split()
    s_new = mutate_string(s, int(i), c)
    print(s_new)

# ==========================================================================================

# Question 18:- Strings

def count_substring(string, sub_string):
    count = 0
    # Loop through the string up to the point where the substring can still fit
    for i in range(len(string) - len(sub_string) + 1):
        # Check if the slice matches the substring
        if string[i : i + len(sub_string)] == sub_string:
            count += 1
            
    return count
        

if __name__ == '__main__':
    string = input().strip()
    sub_string = input().strip()
    
    count = count_substring(string, sub_string)
    print(count)