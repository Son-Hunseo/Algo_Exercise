import sys
from collections import deque

m, n = map(int, input().split())
tomato = []
good_t_loca = []
for i in range(n):
    data = list(map(int, sys.stdin.readline().rstrip().split()))
    tomato.append(data)
    for j in range(len(data)):
        if data[j] == 1:
            good_t_loca.append((i,j))

queue = deque()
# 이렇게 여러개의 시작점이 있는 경우, 시작점 마다 bfs를 돌리는 것이 아니라
# 시작점들을 같은 레벨(층)에 있다고 생각하고 큐에 다 넣어놓고 시작한다.
for start in good_t_loca:
    queue.append((start[0], start[1], 0))

visited = [[False for _ in range(m)] for _ in range(n)]

while queue:
    loca = queue.popleft()
    if (loca[0]<0 or loca[0]>n-1) or (loca[1]<0 or loca[1]>m-1):
        continue
    elif tomato[loca[0]][loca[1]] == -1:
        continue
    elif visited[loca[0]][loca[1]] == True:
        continue
    else:
        visited[loca[0]][loca[1]] = True
        if tomato[loca[0]][loca[1]] == 0:
            tomato[loca[0]][loca[1]] = loca[2]+1
        elif loca[2]+1 < tomato[loca[0]][loca[1]]:
            tomato[loca[0]][loca[1]] = loca[2]+1
        queue.append((loca[0] + 1, loca[1], loca[2]+1))
        queue.append((loca[0] - 1, loca[1], loca[2]+1))
        queue.append((loca[0], loca[1] + 1, loca[2]+1))
        queue.append((loca[0], loca[1] - 1, loca[2]+1))

# 지금 현재 1씩 빼야하는 상황
max_result = 0
min_result = 99999999

for i in range(n):
    max_result = max(max_result, max(tomato[i]))
    min_result = min(min_result, min(tomato[i]))

if (max_result == 1) and (min_result == 1):
    print(0)
else:
    cnt = 0
    for i in range(n):
        if 0 in tomato[i]:
           cnt += 1
    if cnt != 0:
        print(-1)
    else:
        print(max_result - 1)