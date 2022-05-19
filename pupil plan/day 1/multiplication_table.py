# https://codeforces.com/problemset/problem/577/A

n,x = map(int,input().split())

def bruteForce(n,x):
    table = [[0 for _ in range(n)] for __ in range(n)]
    ans = 0
    for i in range(n):
        for j in range(n):
            table[i][j] = (i+1)*(j+1)
            if table[i][j] == x:
                ans += 1
    return ans

bfans = bruteForce(n,x)
print(bfans)