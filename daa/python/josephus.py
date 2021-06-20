# basically here we build from the bottom: 
# when you are at the end, the safest place to be is in 0th place, ie start since only one person is left
# one death earlier, it makes sense that you should not be the kth person from the start , ie if k is 3 and 2 people are left,
#  then you should be in the (0 + 3) % 2 = 1st position after start. if k is 3 and 3 people are left , then you build on this, assuming that the count starts
# from your name after someone is killed. so it will be (1 + 3) % 3 (3 people) = 1st position again after start.
#  build on this again : now 4 people :- so (1 + 3) % 4 = zeroth position after start ie directly the start
#  again : now 5 people :- (0 + 3) % 5 which is 3 ie 3rd position after start ie the index 4
#  so this builds the solution such that for any given n and k, you get the position that you need to stay in so you survive till the end
def josephus(n,k):
    ans = 0
    for size in range(2,n + 1):
        ans = (ans + k) % size
        print(ans + 1,end=" ")
    print(ans)
    return ans

n,k = list(map(int,input().split()))
ans = josephus(n,k)
print("Answer is " ,ans + 1)