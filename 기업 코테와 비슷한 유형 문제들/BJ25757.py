import sys

n, game = map(str, input().split())
n = int(n)

data = []
for _ in range(n):
    name = sys.stdin.readline().rstrip()
    data.append(name)

data = set(data)

if game == "Y":
    print(len(data)//1)
elif game == "F":
    print(len(data)//2)
else:
    print(len(data)//3)