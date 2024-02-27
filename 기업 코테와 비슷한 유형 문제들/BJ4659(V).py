mo = ["a", "e", "i", "o", "u"]

def check(password):
    mo_check = False
    for con in password:
        if con in mo:
            mo_check = True
            break

    three_check = True
    mo_cnt = 0
    ja_cnt = 0
    for con in password:
        if con in mo:
            ja_cnt = 0
            mo_cnt += 1
        else:
            mo_cnt = 0
            ja_cnt += 1
        if (mo_cnt == 3) or (ja_cnt == 3):
            three_check = False
            break

    same_check = True
    before = "abc"
    for con in password:
        # con != ("e" or "o") 이렇게 작성하면 내가 생각하는 것처럼 작동하지 않는다.
        #
        if (con != "e") and (con != "o") and (before == con):
            same_check = False
            break
        before = con

    if (same_check == True) and (mo_check == True) and (three_check == True):
        return True
    else:
        return False

while True:
    data = input()
    if data == "end":
        break
    result = check(data)
    if result == True:
        print("<" + data + ">" + " is acceptable.")
    else:
        print("<" + data + ">" + " is not acceptable.")