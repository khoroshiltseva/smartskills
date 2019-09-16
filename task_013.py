def Unmanned(L, N, track):
    current_point = track[0][0]
    current_time = track[0][0]

    for i in range(len(track)):
        current_time += track[i][0] - current_point
        n = current_time
        red = True
        for j in range(track[i][0] // 2 + 1):
            if n - track[i][1] <= 0:
                n = -(n - track[i][1])
                break
            elif n - track[i][1] - track[i][2] >= 0:
                n = n - track[i][1] - track[i][2]
            else:
                red = False
                break
        if red == True:
            current_time += n
        current_point = track[i][0]

    current_time += L - current_point

    return current_time
