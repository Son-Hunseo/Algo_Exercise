import sys

n = int(input())

road = list(map(int, sys.stdin.readline().rstrip().split()))
city = list(map(int, sys.stdin.readline().rstrip().split()))

dp_table = []

bf = 1000000001

for i in range(len(road)):
    dp_table.append(road[i]*min(bf, city[i]))
    if city[i] < bf:
        bf = city[i]

print(sum(dp_table))