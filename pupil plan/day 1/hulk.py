# https://codeforces.com/problemset/problem/705/A

n = int(input())
def printSol(n):
    ans = ""
    for i in range(n):
        if i % 2 == 0:
            ans += "I hate "
            pass
        else:
            ans += "I love "
            pass
        if i == n-1:
            ans += "it"
            pass
        else:
            ans += "that "
            pass
    print(ans)
    pass
printSol(n)