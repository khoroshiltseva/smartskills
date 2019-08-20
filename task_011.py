def MassVote(N, Votes):
    if N == 1 and Votes[0] > 50:
        return "majority winner 1"
    elif N == 1 and Votes[0] <= 50:
        return "minority winner 1"

    winner = 1
    max_num = Votes[0]
    for i in range(1, len(Votes)):
        if Votes[i] > max_num:
            max_num = Votes[i]
            winner = i + 1

    n = 0
    for i in range(len(Votes)):
        if Votes[i] == max_num:
            n += 1

    if n > 1:
        return "no winner"

    if n == 1 and max_num > 50:
        return "majority winner %s" % (winner)
    else:
        return "minority winner %s" % (winner)
