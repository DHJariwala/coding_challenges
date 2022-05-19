# https://codeforces.com/contest/807/problem/A

n = int(input())
ratings = []
for _ in range(n):
    ratings.append(list(map(int,input().split())))

def isRated(ratings):
    for x in ratings:
        if x[0] != x[1]:
            return "rated"
    flag = 1
    for i in range(1,len(ratings)):
        if ratings[i][1] > ratings[i-1][1]:
            flag = 0
            break
    if flag:
        return "maybe"
    else:
        return "unrated"

ans = isRated(ratings)
print(ans)    