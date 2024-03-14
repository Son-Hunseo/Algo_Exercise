import sys

n, x = map(int, input().split())
data = list(map(int, sys.stdin.readline().rstrip().split()))

result = []
cur = sum(data[0:x])
max = cur
result.append(cur)
for i in range(n-x):
    cur -= data[i]
    cur += data[i+x]
    if cur > max:
        max = cur
    result.append(cur)

if result:
    if max == 0:
        print("SAD")
    else:
        print(max)
        print(result.count(max))
else:
    print("SAD")