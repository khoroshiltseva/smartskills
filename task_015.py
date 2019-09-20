def LineAnalysis(line):

    line_arr = list(line)

    if "." in line_arr == False:
        return True

    if line_arr[0] != "*":
        return False

    stars = ""
    stars_arr = []
    for i in range(len(line_arr)):
        if line_arr[i] == "*":
            stars += line_arr[i]
        elif stars == "":
            continue
        else:
            stars_arr.append(stars)
            stars = ""
    stars_arr.append(stars)

    stars = stars_arr[0]
    for i in range(len(stars_arr)):
        if stars_arr[i] != stars:
            return False

    dots = ""
    dots_arr = []
    for i in range(len(stars), len(line_arr)):
        if line_arr[i] == ".":
            dots += line_arr[i]
        elif dots == "":
            continue
        else:
            dots_arr.append(dots)
            dots = ""

    if len(dots_arr) + 1 != len(stars_arr):
        return False

    dots = dots_arr[0]
    for i in range(len(dots_arr)):
        if dots_arr[i] != dots:
            return False

    return True

