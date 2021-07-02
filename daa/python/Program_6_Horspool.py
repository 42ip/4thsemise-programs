# # Q:6
# Algorithm to implement string matching using horspool's algorithm
# Time complexity : O(nlogn), where n is length of array. 
# Space complexity : O(n) ,where we divide the problem into n subproblems



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
        while  (k < n) and string[i - k] == pattern[m - 1 - k] : 
            k += 1
        if k == m  : return i - m + 1
        else : 
            if  (string[i] in table) is not True : table[string[i]] = m
            i = i + table[string[i]]
    print(table)
    if i >= m : return "not possible!"
print(horspool('a',"aaa"))