import sys
input = sys.stdin.readline

n,m = map(int, input().split())
d = {}
for _ in range(n):
    name = input().strip()

    if len(name) < m:
        continue
        # d.get()은 해당 값이 존재하면 값을 반환 없으면 None을 반환
    if d.get(name):
        # 단어가 존재하면 개수 하나 증가
        d[name][0] += 1
    else:
        # 존재하지 않으면 [개수, 길이, 단어] 추가
        d[name] = [1, len(name), name]

print(d)
# 개수, 길이는 내림차순으로 단어는 사전순(오름차순)으로 정렬
# 여기서 d.items() 는 딕셔너리 안의 값들을 (키, 밸류)형식의 값들의 리스트로 반환한다.
# 따라서 x[1]은 각 값의 밸류를 뜻하며 x[1][0]은 각 단어의 개수를 의미한다.
ans = sorted(d.items(), key= lambda x: (-x[1][0], -x[1][1], x[1][2]))

for a in ans:
    print(a[0])