n = int(input())

data = [[0, 1, 2, 3, 4, 5, 6, 7, 8, 9]]

for _ in range(9):
    new_data = []
    for i in range(len(data[-1])):
        if int(str(data[-1][i])[-1]) != 0:
            for j in range(int(str(data[-1][i])[-1])-1, -1, -1):
                new_data.append(int(str(data[-1][i])+str(j)))
    data.append(new_data)

result = []
for i in range(len(data)):
    for j in range(len(data[i])):
        result.append(data[i][j])

result.sort()

if n >= len(result):
    print(-1)
else:
    print(result[n])