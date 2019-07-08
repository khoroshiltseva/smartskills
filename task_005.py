def PatternUnlock(N, hits):
    hits_sum = N - 1

    x = [[6, 1, 9], [5, 2, 8], [4, 3, 7]]
    y = [[6, 5, 4], [1, 2, 3], [9, 8, 7]]

    for i in range(len(hits) - 1):
        for j in range(len(x)):
            if hits[i] in x[j] and hits[i + 1] not in x[j]:
                for k in range(len(y)):
                    if hits[i] in y[k] and hits[i + 1] not in y[k]:
                        hits_sum += 0.41421
                        break

    s1 = str(round(hits_sum, 5))

    s1_arr = list(s1)

    s2_arr = []

    for i in range(len(s1_arr)):
        if s1_arr[i] != "0" and s1_arr[i] != ".":
            s2_arr.append(s1_arr[i])

    s2 = "".join(s2_arr)

    return s2
