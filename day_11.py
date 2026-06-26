# Question 22:- String > Text wrap

# Getting familiar with text wrap function....
import textwrap

line = "Hello Everyone, Here I am showing you all how I approach questions and finally solves them."
# print(textwrap.wrap(line, 5))
# print(textwrap.wrap(line, 8))
# print(textwrap.wrap(line, 12))

# print(textwrap.fill(line, 5))
# print(textwrap.fill(line, 8))
print(textwrap.fill(line, 12))

# Solution 
import textwrap

def wrap(string, max_width):
    return textwrap.fill(string, max_width)

if __name__ == '__main__':
    string, max_width = input(), int(input())
    result = wrap(string, max_width)
    print(result)