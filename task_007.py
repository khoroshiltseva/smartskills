def SumOfThe(N, data):
    result = 0

    for i in range(len(data)):
        summ = 0
        for j in range(len(data)):
            summ += data[j]
        summ -= data[i]
        if data[i] == summ:
            result = data[i]

    return result

