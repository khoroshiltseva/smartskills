def HowManyTimes(s, s_generic):
    a = list(s_generic)
    b = list(s)

    b1 = b[:]

    a1 = []
    for i in range(len(a)):
        if len(b1) != 0:
            for j in range(len(b1)):
                if a[i] == b1[0]:
                    a1.append(b1[0])
                    del b1[0]
                    break

    if len(a1) != len(b):
        return 0
    else:
        for i in range(len(b)):
            for j in range(len(b1)):
                if b[i] != b1[j]:
                    return 0

    c = a[:]

    d = []
    e = []
    for i in range(len(b) - 1):
        while c[0] != b[i + 1]:
            if c[0] == b[i]:
                e.append(i)
                del c[0]
            else:
                del c[0]
        d.append(e)
        e = []

    while len(c) != 0:
        if c[0] == b[-1]:
            e.append(b.index(b[-1]))
        del c[0]

    d.append(e)

    res = 1

    for i in range(len(d)):
        res *= len(d[i])

    return res

