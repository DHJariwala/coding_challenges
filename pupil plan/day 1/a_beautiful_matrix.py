# https://codeforces.com/contest/263/problem/A

matrix = []
for _ in range(5):
    matrix.append(list(map(int,input().split())))

def beautifyMatrix(mat):
    oneIndex = (0,0)
    for i in range(5):
        for j in range(5):
            if mat[i][j] == 1:
                oneIndex = (i,j)
                break
    return abs(oneIndex[0] - 2) + abs(oneIndex[1] - 2)


ans = beautifyMatrix(matrix)
print(ans)    