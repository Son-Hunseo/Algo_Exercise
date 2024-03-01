T = int(input())

for _ in range(T):
    n = int(input())
    score = [999]
    data = list(map(int, input().split()))
    score = score + data
    candi = set(score[1:])

    qual_candi = [0 for _ in range(len(candi)+1)]
    for i in range(1, len(score)):
        qual_candi[score[i]] += 1

    qual = []
    for i in range(len(qual_candi)):
        if qual_candi[i] == 6:
            qual.append(i)

    candi_score = [0]
    for con in score:
        if con in qual:
            candi_score.append(con)
    score = candi_score

    board = [[] for _ in range(len(candi)+1)]
    for con in qual:
        for i in range(1, len(score)):
            if score[i] == con:
                board[con].append(i)

    final_score = [0]
    for i in range(1, len(board)):
        final_score.append(sum(board[i][:4]))

    for i in range(1, len(final_score)):
        if i not in qual:
            final_score[i] = 99999999

    winner_score = min(final_score[1:])
    winner = []
    for i in range(1, len(final_score)):
        if final_score[i] == winner_score:
            winner.append(i)

    if len(winner) != 1:
        final_winner = 0
        min_fourth = 99999999
        for con in winner:
            if board[con][4] < min_fourth:
                final_winner = con
                min_fourth = board[con][4]
    else:
        final_winner = winner[0]

    print(final_winner)