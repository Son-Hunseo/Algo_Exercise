import sys
sys.setrecursionlimit(1000000000)
# recursionlimit 설정 알아두기

def dfs(bachu, row, col):
    if (row<0 or row>(len(bachu)-1)) or (col<0 or col>(len(bachu[0])-1)):
        return False
    elif bachu[row][col] == 0:
        return False
    else:
        bachu[row][col] = 0
        dfs(bachu, row + 1, col)
        dfs(bachu, row - 1, col)
        dfs(bachu, row, col + 1)
        dfs(bachu, row, col - 1)
        return True

T = int(input())
for _ in range(T):
    M, N, K = map(int, input().split())
    bachu = [[0 for _ in range(M)] for _ in range(N)]
    for _ in range(K):
        X, Y = map(int, input().split())
        bachu[Y][X] = 1
    cnt = 0
    for i in range(N):
        for j in range(M):
            if bachu[i][j] == 1:
                cnt += 1
                dfs(bachu, i, j)
    print(cnt)