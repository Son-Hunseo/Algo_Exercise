import sys

p = int(input())
for _ in range(p):
    data = list(map(int, sys.stdin.readline().rstrip().split()))
    num = data[0]
    data = data[1:]
    step = 0
    cur_data = []
    for i in range(20):
        cur_data.append(data[i])
        for j in range(len(cur_data)):
            if (cur_data[i] < cur_data[j]) and i > j:
                cur = cur_data[i]
                cur_data[j+1:i+1] = cur_data[j:i]
                cur_data[j] = cur
                step += (i-j)
    print(num, step)