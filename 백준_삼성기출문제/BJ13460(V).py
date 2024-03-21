# 해설강의 참조했음
n, m = map(int, input().split())
graph = []
for _ in range(n):
    data = list(input())
    graph.append(data)

for i in range(n):
    for j in range(m):
        if graph[i][j] == "R":
            ri, rj = i, j
        if graph[i][j] == "B":
            bi, bj = i, j

di = [-1, 1, 0, 0]
dj = [0, 0, -1, 1]
v_set = set()

def move(i, j, dr):
    back = -1
    for cnt in range(1, 10):
        ni = i + di[dr]*cnt
        nj = j + dj[dr]*cnt
        if graph[ni][nj] == "#":
            return cnt + back
        if graph[ni][nj] == "O":
            return cnt
        if graph[ni][nj] == "R" or graph[ni][nj] == "B":
            back += -1

ans = 11

def dfs(ri, rj, bi, bj, cnt):
    # 가지치기
    if (ri, rj, bi, bj, cnt) in v_set:
        return
    v_set.add((ri, rj, bi, bj, cnt))

    if cnt > 10:
        return

    global ans
    for dr in range(4):
        rm = move(ri, rj, dr)
        bm = move(bi, bj, dr)

        if rm == 0 and bm == 0:
            continue

        nri = ri + di[dr]*rm
        nrj = rj + dj[dr]*rm
        nbi = bi + di[dr]*bm
        nbj = bj + dj[dr]*bm

        if graph[nbi][nbj] == "O":
            continue
        else:
            if graph[nri][nrj] == "O":
                ans = min(ans, cnt)
                return

        # 실제 그래프 이동시켜줘야함
        graph[ri][rj], graph[bi][bj] = ".", "."
        graph[nri][nrj], graph[nbi][nbj] = "R", "B"
        dfs(nri, nrj, nbi, nbj, cnt + 1)
        graph[nri][nrj], graph[nbi][nbj] = ".", "."
        graph[ri][rj], graph[bi][bj] = "R", "B"

dfs(ri, rj, bi, bj, 1)
if ans == 11:
    ans = -1
print(ans)