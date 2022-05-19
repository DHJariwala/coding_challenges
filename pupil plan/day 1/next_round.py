# https://codeforces.com/contest/158/problem/A

n,k = map(int,input().split())
points = list(map(int,input().split()))

def nextRoundContestants(k,points):
    kvalue = points[k-1]
    ans = 0
    for x in points:
        if x >= kvalue and x != 0:
            ans += 1
    return ans

ans = nextRoundContestants(k,points)
print(ans)