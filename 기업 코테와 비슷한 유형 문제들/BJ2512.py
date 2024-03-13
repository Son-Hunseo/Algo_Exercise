import sys

n = int(input())
data = list(map(int, sys.stdin.readline().rstrip().split()))
m = int(input())

candi = []


def bs(start, end):
    if start > end:
        return
    mid = (start + end) // 2
    result = 0
    for con in data:
        if con > mid:
            result += mid
        else:
            result += con
    if result == m:
        candi.append(mid)
        return
    if result > m:
        bs(start, mid - 1)
    if result < m:
        candi.append(mid)
        bs(mid + 1, end)

# 왜 문제에서는 n이라고 해놓고 1로하니까 정답이 되는거지?!?!
bs(1, 1000000000)
if candi:
    if max(candi) > max(data):
        print(max(data))
    else:
        print(max(candi))
else: # 이거 고려했어야함
    print(max(data))