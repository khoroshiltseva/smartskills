def squirrel(N):
    factorial = 1
    while N > 1:
        factorial *= N
        N = N - 1
    return (int(str(factorial)[0]))
