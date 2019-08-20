def UFO(N, data, octal):
    res = []
    if octal:
        for i in range(N):
            current = str(data[i])
            num = 0
            for j in range(len(current)):
                num += int(current[j]) * (8 ** (len(current) - 1 - j))
            res.append(num)
            num = 0
    else:
        for i in range(N):
            current = str(data[i])
            num = 0
            for j in range(len(current)):
                num += int(current[j]) * (16 ** (len(current) - 1 - j))
            res.append(num)
            num = 0
    return res