n = int(input())
x = 1
cnt = 0

while True:
    if n == 1:
        print(1)
        break
    x += 1
    cnt += 1
    y = ((x - 1) + (6 * cnt))
    if x <= n <= y:
        print(cnt+1)
        break
    x = y