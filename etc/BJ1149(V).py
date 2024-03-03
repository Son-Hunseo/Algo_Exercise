import sys

n = int(input())

data = []
for _ in range(n):
    row = list(map(int, sys.stdin.readline().rstrip().split()))
    data.append(row)

dp_table = [data[0][0], data[0][1], data[0][2]]

for i in range(1, n):
    # b_dp_table = dp_table
    # 파이썬에서 위처럼 리스트(혹은 사전형 자료형)를 선언하면 해당 변수가 원래 자료형을 가리키게된다. (레퍼런스 변수)
    b_dp_table = [dp_table[0], dp_table[1], dp_table[2]]
    for j in range(3):
        if j == 0:
            dp_table[j] = data[i][j] + min(b_dp_table[1], b_dp_table[2])
        elif j == 1:
            dp_table[j] = data[i][j] + min(b_dp_table[0], b_dp_table[2])
        else:
            dp_table[j] = data[i][j] + min(b_dp_table[0], b_dp_table[1])

print(min(dp_table))