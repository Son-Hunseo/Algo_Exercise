# 문자열에서 in 은 연속된 것만 확인 11 in 101은 False 이다.
n = input()

cnt = 0
while True:
    if len(n) == 0:
        break
    cnt += 1
    for i in range(len(str(cnt))):
        if len(n) == 0:
            break
        if n[0] == str(cnt)[i]:
            n = n[1:]
print(cnt)