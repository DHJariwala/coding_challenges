# https://codeforces.com/problemset/problem/520/A

n = int(input())
s = input()

def isPanagram(s):
    s = s.lower()
    alphabet = "abcdefghijklmnopqrstuvwxyz"
    for x in s:
        if x in alphabet:
            alphabet = alphabet.replace(x,'')
        else:
            continue
    if alphabet == "":
        return True
    else:
        return False

if isPanagram(s):
    print("YES")
else:
    print("NO")