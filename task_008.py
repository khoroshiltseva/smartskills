def HowManyTimes(s, s_generic):
    sg_arr = list(s_generic)
    s_arr = list(s)

    sg_index = []
    current = []
    for i in range(len(s_arr)):
        for j in range(len(sg_arr)):
            if sg_arr[j] == s_arr[i]:
                current.append(j)
        sg_index.append(current)
        current = []

    res_arr = []
    for i in range(len(sg_index[0])):
        res_arr.append([sg_index[0][i]])

    current_arr = []
    current2 = []
    for i in range(1, len(sg_index)):
        for j in range(len(res_arr)):
            for k in range(len(sg_index[i])):
                if res_arr[j][-1] < sg_index[i][k]:
                    current2 = res_arr[j] + [sg_index[i][k]]
                    current_arr.append(current2)
                    current2 = []
        res_arr = current_arr
        current_arr = []

    return len(res_arr)

