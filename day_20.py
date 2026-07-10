# Question 32:- Sets > Introduction to Sets 
# to find average 

def average(array):
    # your code goes here

    # this code doesn't working as this question is asking for set. 
    # s = 0
    # l = len(array)
    # for i in set(set(array)):
    #     s += i
    # return s/len(array)

    # it converts array into set 
    # print(set(array)) 
    
    s = 0 
    for i in set(array):
        s += i
    l = len(set(array))
    avg = s/l
    return avg

if __name__ == '__main__':
    n = int(input())
    arr = list(map(int, input().split()))
    result = average(arr)
    print(result)