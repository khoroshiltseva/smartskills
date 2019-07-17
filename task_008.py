def HowManyTimes(s, s_generic):

    a = list(s_generic)
    b = list(s)

    n = 1
    result = 1

    for i in range(len(b)):
        for j in range(len(a)):
            if b[i] == a[i]:
                result *= n
                n = 1
                break
            elif b[i] != a[i]:
                n += 1
                del a[i]
                break

    result *= n
    n = 1 + (len(a) - len(b))
    result *= n

    return result

