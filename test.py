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

print(word_dict.items())