import sys

n, k = map(int, input().split())
data = []
result = [0 for _ in range(n+1)]
for _ in range(n):
    country, gold, silver, bronze = map(int, sys.stdin.readline().rstrip().split())
    data.append((gold, silver, bronze, country))

data.sort(reverse=True)
for i in range(1, len(data)+1):
    if i > 1:
        if data[i-1][0:3] == before:
            result[data[i-1][3]] = result[data[i-2][3]]
        else:
            result[data[i-1][3]] = i
    else:
        result[data[i-1][3]] = i
    before = data[i-1][0:3]

print(result[k])