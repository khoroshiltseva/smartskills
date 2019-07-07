def PatternUnlock(N, hits):
    hits_sum = 0

    for i in range(N - 1):
        if abs(hits[i] - hits[i + 1]) == 1:
            hits_sum += 1
        else:
            hits_sum += 2 ** 0.5

    s1 = str(round(hits_sum, 5))
    s1_arr = list(s1)

    s2_arr = []

    for i in range(len(s1_arr)):
        if s1_arr[i] != "0" and s1_arr[i] != ".":
            s2_arr.append(s1_arr[i])

    s2 = "".join(s2_arr)

    return s2


