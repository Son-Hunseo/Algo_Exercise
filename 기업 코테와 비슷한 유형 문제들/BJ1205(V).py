# 이 문제에서의 n<p 와 같은 예외사항을 잘 고려하자
# 문제를 꼼꼼하게 읽자

n, new, p = map(int, input().split())
rank = []
only_num = []

if n != 0:
    input_list = list(map(int, input().split()))
    input_list.append(new)
    input_list.sort(reverse=True)
    if n > p:
        input_list = input_list[:p]

    bf = 9999999999
    for i in range(len(input_list)):
        only_num.append(input_list[i])
        if input_list[i] < bf:
            rank.append((i+1, input_list[i]))
            bf = input_list[i]
        else:
            rank.append((rank[i-1][0], input_list[i]))
            bf = input_list[i]

    if n < p:
        for i in range(len(rank)):
            if rank[i][1] == new:
                print(rank[i][0])
                break
    else:
        for i in range(len(rank)):
            if new <= min(only_num):
                print(-1)
                break
            else:
                if rank[i][1] == new:
                    print(rank[i][0])
                    break
else:
    print(1)