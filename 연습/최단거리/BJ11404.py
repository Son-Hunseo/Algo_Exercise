import sys

INF = 99999999

n = int(input())
m = int(input())

distance_data = [[INF for _ in range(n+1)] for _ in range(n+1)]

for _ in range(m):
    i, j, distance = map(int, sys.stdin.readline().rstrip().split())
    if distance < distance_data[i][j]:
        distance_data[i][j] = distance

# 출발점과 시작점이 같은 곳은 0으로 초기화
for i in range(n+1):
    for j in range(n+1):
        if i == j:
            distance_data[i][j] = 0

for k in range(1, n+1):
    for i in range(1, n+1):
        for j in range(1, n+1):
            distance_data[i][j] = min(distance_data[i][j], distance_data[i][k]+distance_data[k][j])

for i in range(1, n+1):
    for j in range(1, n+1):
        if distance_data[i][j] == INF:
            distance_data[i][j] = 0
        if j == n:
            print(distance_data[i][j])
        else:
            print(distance_data[i][j], end=" ")