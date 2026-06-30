# Question 26:- String < Capatalize
s = "hello world"
s1 = "123hello world"
s2 = "123hello 546world"
s3 = "a123di"

print(s3.title())

def solve(s):
    # Split by a SINGLE space to preserve consecutive space counts
    words = s.split(' ')
    
    # Capitalize only the first character of each word
    capitalized_words = [word.capitalize() for word in words]
    
    # Join them back together with a single space
    return ' '.join(capitalized_words)