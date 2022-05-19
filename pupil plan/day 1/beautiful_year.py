# https://codeforces.com/problemset/problem/271/A

n = int(input())

def nextBeautifulYear(n):
    year = n+1
    while True:
        sYear = str(year)
        if len(set(sYear)) == 4:
            break
        year += 1
    return year

ans = nextBeautifulYear(n)
print(ans)