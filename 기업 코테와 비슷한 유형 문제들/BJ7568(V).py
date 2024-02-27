import sys

n = int(input())

data = []
result = [0 for _ in range(n)]

for i in range(n):
    x, y = map(int, sys.stdin.readline().strip().split())
    data.append((y, x, i))

data.sort(reverse=True)

bf_height, bf_weight = 10000, 10000
candi = []
for i in range(n):
    if i == 0:
        result[data[i][2]] = i+1
        candi.append(data[i])
    else:
        ## 문제 좀 잘 읽자 그냥 덩치가 더 큰 사람의 수를 일일이 완전 탐색으로
        ## 세면 되는건데 자꾸 어떠한 조건문을 걸어서 처리하려고 했다.
        cnt = 0
        for con in data:
            if (con[0] > data[i][0]) and (con[1] > data[i][1]):
                cnt += 1

        result[data[i][2]] = cnt + 1

print(*result)