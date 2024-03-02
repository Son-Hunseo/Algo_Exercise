import sys

n = int(input())
m = int(input())

location = list(map(int, sys.stdin.readline().rstrip().split()))
distance = []

for i in range(m+1):
    if i == m:
        distance.append(n-location[i-1])
    elif i == 0:
        distance.append(location[i]-0)
    else:
        distance.append(location[i]-location[i-1])

for i in range(len(distance)):
    if (i != 0) and i != (len(distance)-1):
        if (distance[i]/2)%1 == 0:
            distance[i] = distance[i]//2
        else:
            distance[i] = int(distance[i]//2)+1

print(max(distance))