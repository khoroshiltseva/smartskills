def HowManyTimes(s, s_generic):
    a = list(s_generic)
    b = list(s)

    for i in range(len(b)):
        for j in range(len(a)):
            if b[i] == a[j]:
                del a[j]
                break

    return 2 ** len(a)
