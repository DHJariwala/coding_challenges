# https://codeforces.com/contest/732/problem/A

k,r = map(int,input().split())

def minNoShovel(k,r):
    ctr = 1
    while True:
        a = ctr*k - r
        b = ctr*k
        if b%10 == 0:
            break
        if a % 10 == 0:
            break
        ctr += 1
        pass
    return ctr

ans = minNoShovel(k,r)
print(ans)
