def ConquestCampaign(N, M, L, battalion):

    days = 1

    all_dots = set()
    for i in range(0, len(battalion), 2):
        t = tuple([battalion[i], battalion[i + 1]])
        all_dots.add(t)

    current_dots = []
    for i in range(0, len(battalion), 2):
        t = tuple([battalion[i], battalion[i + 1]])
        current_dots.append(t)

    new_dots = []

    for i in range((N * M // 2)):
        if len(all_dots) == N * M:
            return days
        days += 1
        for x, y in current_dots:
            if 1 <= x <= N and 1 <= y + 1 <= M and (x, y + 1) not in all_dots:
                new_dots.append((x, y + 1))
                all_dots.add((x, y + 1))
            if 1 <= x <= N and 1 <= y - 1 <= M and (x, y - 1) not in all_dots:
                new_dots.append((x, y - 1))
                all_dots.add((x, y - 1))
            if 1 <= x + 1 <= N and 1 <= y <= M and (x + 1, y) not in all_dots:
                new_dots.append((x + 1, y))
                all_dots.add((x + 1, y))
            if 1 <= x - 1 <= N and 1 <= y <= M and (x - 1, y) not in all_dots:
                new_dots.append((x - 1, y))
                all_dots.add((x - 1, y))
            if len(all_dots) == N * M:
                break
        current_dots = new_dots
        new_dots = []

    return days
