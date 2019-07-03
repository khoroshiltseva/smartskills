def odometer(oksana):
    distance = 0
    timepass = 0
    for i in range(0, len(oksana), 2):
        distance += oksana[i] * (oksana[i + 1] - timepass)
        timepass = oksana[i + 1]
    return distance
