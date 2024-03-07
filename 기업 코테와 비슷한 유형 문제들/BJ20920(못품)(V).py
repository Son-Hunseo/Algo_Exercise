import sys

n, m = map(int, input().split())
word_dict = {}

for i in range(n):
    word = sys.stdin.readline().rstrip()
    if len(word) < m:
        continue

    if word in word_dict.keys():
        word_dict[word][0] += 1
    else:
        word_dict.update({word: [1, len(word), word]})

# dict.values() : 딕셔너리 안의 밸류만 다 꺼내서 리스트 형태(리스트와 비슷한)로 저장
# dict.keys() : 딕셔너리 안의 키만 다 꺼내서 리스트 형태(리스트와 비슷한)로 저장
# dict.items() : 딕셔너리 안의 키, 밸류 다 꺼내서 (키, 밸류) 형태의 원소를 가진 리스트 형태(리스트와 비슷한)로 저장
word_list = list(word_dict.values())

def logic(data): # 이렇게 여러 요소를 가지고 정렬할 때 내림차순일 경우 - 를 붙이는 테크닉 필요
    return [-data[0], -data[1], data[2]]

word_list.sort(key=logic)

for con in word_list:
    print(con[2])