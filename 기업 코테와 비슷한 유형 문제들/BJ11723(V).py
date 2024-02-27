import sys

m = int(input())
S = []

for _ in range(m):
    # 경우에 따라 입력받는 개수 다를 경우 리스트로 처리
    data = list(map(str, sys.stdin.readline().rstrip().split()))
    if len(data) == 2:
        data[1] = int(data[1])

    if data[0] == "add":
        if data[1] not in S:
            S.append(data[1])
    elif data[0] == "remove":
        if data[1] in S:
            S.remove(data[1])
    elif data[0] == "check":
        if data[1] in S:
            print(1)
        else:
            print(0)
    elif data[0] == "toggle":
        if data[1] not in S:
            S.append(data[1])
        else:
            S.remove(data[1])
    elif data[0] == "all":
        S = [i for i in range(1, 21)]
    elif data[0] == "empty":
        S = []