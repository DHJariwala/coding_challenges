# https://codeforces.com/problemset/problem/680/B
n,a = map(int,input().split())
cities = list(map(int,input().split()))

def bcd(a,n,cities):
    ctr = 0
    res = 0
    while a-1+ctr < n or a-1-ctr >= 0:
        if cities[a-1+ctr] == 1 and cities[a-1-ctr] == 1:
            if ctr == 0:
                res += 1
            else:
                res += 2
        elif cities[a-1+ctr] == 1 and a-1-ctr < 0:
            res += 1
        elif cities[a-1-ctr] == 1 and a-1+ctr >= n:
            res += 1
        ctr += 1
        pass
    return res

ans = bcd(a,n,cities)
print(ans)