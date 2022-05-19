# https://codeforces.com/problemset/problem/621/A

n = int(input())
num = list(map(int,input().split()))

def maxEvenSum(nums):
    minOdd = 10**9 + 1
    sum = 0
    for x in nums:
        sum += x
        if x < minOdd and x % 2 == 1:
            minOdd = x
    if sum%2 == 0:
        return sum
    else:
        return sum-minOdd    

ans = maxEvenSum(num)
print(ans)