import sys
import heapq

V, E = map(int, input().split())
k = int(input())
edge = [[] for _ in range(V+1)]
INF = 9999999999

for i in range(E):
    u, v, w = map(int, sys.stdin.readline().rstrip().split())
    edge[u].append((w, v))

# 우선순위 큐로 다익스트라 구현할 때는 방문처리 x // 그냥 더 작으면 갱신해주는 로직만 넣으면 됨
def dijkstra(start):
    q = []
    result = [INF for _ in range(V+1)]
    result[start] = 0
    heapq.heappush(q, (0, start))
    while q:
        cur = heapq.heappop(q)
        # 여기
        if result[cur[1]] < cur[0]:
            continue
        for con in edge[cur[1]]:
            if result[con[1]] > (result[cur[1]]+con[0]):
                result[con[1]] = result[cur[1]]+con[0]
                heapq.heappush(q, (result[con[1]], con[1]))
    return result

result = dijkstra(k)

for i in range(1, len(result)):
    if result[i] >= INF:
        print("INF")
    else:
        print(result[i])