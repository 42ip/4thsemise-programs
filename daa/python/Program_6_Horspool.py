# # Q:6
# Algorithm to implement string matching using horspool's algorithm
# Time complexity : O(nm), where n is length of string is n and length of pattern is m. 
# Space complexity : O(n) ,where we divide the problem into n subproblems


# INPUT PORTION
# uncomment below for preconfigured input
pattern = 'hello'
string = 'i wanted to say hello everyone'

# uncomment below for entering your own input
print('Enter string') ; string = input()
print('Enter pattern'); pattern = input()

# PROGRAM PORTION
def shifttable(string):
    dict = {}
    for i in range(0,len(string) - 1):
        dict[string[i]] = len(string) - i - 1
    print(dict)
    return dict
def horspool(pattern, string):
    m = len(pattern)
    n = len(string)
    table = shifttable(pattern)
    i = m - 1
    while i <= n - 1  :
        k = 0
        while  (k < m) and string[i - k] == pattern[m - 1 - k] : 
            k += 1
        if k == m  : return i - m + 1
        else : 
            if  (string[i] in table) is not True : table[string[i]] = m
            i = i + table[string[i]]
    if i >= m : return "not possible!"
print(horspool(pattern, string))