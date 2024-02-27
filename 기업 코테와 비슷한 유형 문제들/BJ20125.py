import sys

n = int(input())
data = []

for _ in range(n):
    row = sys.stdin.readline().rstrip()
    data.append(row)

before = "&"
for i in range(1, n):
    for j in range(len(data[i])):
        if (before == "*") and (data[i][j] == "*") and data[i-1][j] == "*":
            heart = (i, j)
            break
        before = data[i][j]

def left_arm(heart_row, heart_col):
    left_arm = 0
    while heart_col>0:
        if data[heart_row][heart_col-1] == "*":
            left_arm += 1
            heart_col -= 1
        else:
            return left_arm
    return left_arm

def right_arm(heart_row, heart_col):
    right_arm = 0
    while heart_col<(n-1):
        if data[heart_row][heart_col+1] == "*":
            right_arm += 1
            heart_col += 1
        else:
            return right_arm
    return right_arm

def body(heart_row, heart_col):
    body = 0
    while True:
        if data[heart_row+1][heart_col] == "*":
            body += 1
            heart_row += 1
        else:
            return body

def left_leg(body_row, body_col):
    left_leg = 0
    body_col -= 1
    while body_row < n-1:
        if data[body_row+1][body_col] == "*":
            left_leg += 1
            body_row += 1
        else:
            return left_leg
    return left_leg

def right_leg(body_row, body_col):
    right_leg = 0
    body_col += 1
    while body_row < n-1:
        if data[body_row+1][body_col] == "*":
            right_leg += 1
            body_row += 1
        else:
            return right_leg
    return right_leg

print(str(heart[0]+1), str(heart[1]+1))
result = []
result.append(left_arm(heart[0], heart[1]))
result.append(right_arm(heart[0], heart[1]))
body = body(heart[0], heart[1])
result.append(body)
body_row, body_col = heart[0]+body, heart[1]
result.append(left_leg(body_row, body_col))
result.append(right_leg(body_row, body_col))
print(*result)