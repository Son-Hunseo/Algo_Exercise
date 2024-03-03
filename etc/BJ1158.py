n, k = map(int, input().split())

data = [i for i in range(1, n+1)]
result = []

cur_idx = k
while data:
    if len(data) != 1:
        target = data[(cur_idx-1)%len(data)]
        nxt = data[cur_idx%len(data)]
        result.append(target)
        data.remove(target)
        nxt_idx = data.index(nxt)
        cur_idx = (nxt_idx + k)%(len(data))
    else:
        result.append(data[0])
        data.pop()

print("<", end="")
for i in range(len(result)):
    if i == len(result)-1:
        print(result[i], end="")
    else:
        print(result[i], end=", ")
print(">")