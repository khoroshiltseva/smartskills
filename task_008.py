def HowManyTimes(s, s_generic):
    a = list(s_generic)
    b = list(s)

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
