import sys

input = sys.stdin.readline

n = int(input())

switch = [2]
data = list(map(int, input().split()))
switch = switch + data

k = int(input())
for _ in range(k):
    sex, num = map(int, input().split())
    # 남자일 때
    if sex == 1:
        T = [i*num for i in range(1,(n//num)+1)]
        for con in T:
            if switch[con] == 0:
                switch[con] = 1
            else:
                switch[con] = 0
    # 여자일 때
    else:
        if switch[num] == 0:
            switch[num] = 1
        else:
            switch[num] = 0

        for i in range(1, min(num-1, n-num)+1):
            if switch[num-i] == switch[num+i]:
                if switch[num-i] == 0:
                    switch[num-i] = 1
                else:
                    switch[num-i] = 0

                if switch[num+i] == 0:
                    switch[num+i] = 1
                else:
                    switch[num+i] = 0
            else:
                break

for i in range(1, len(switch)):
    if (i % 20) == 0:
        print(switch[i])
    else:
        print(switch[i], end=" ")