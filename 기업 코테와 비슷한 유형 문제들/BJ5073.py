a, b, c = 1001, 1001, 1001

while True:
    a, b, c = map(int, input().split())
    if a == 0 and b == 0 and c == 0:
        break
    if ((a+b) <= c) or ((b+c) <= a) or ((c+a) <= b):
        print("Invalid")
    elif a == b == c:
        print("Equilateral")
    elif (a != b) and (b != c) and (c != a):
        print("Scalene")
    else:
        print("Isosceles")