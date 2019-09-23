def ShopOLAP(N, items):
    items.sort()

    items_num = []
    for i in range(len(items)):
        a = items[i].split(" ")
        items_num.append(a)

    items_sum = [items_num[0]]
    for i in range(1, len(items_num)):
        if items_num[i][0] == items_sum[-1][0]:
            items_sum[-1][1] = str(int(items_num[i][1]) + int(items_sum[-1][1]))
        else:
            items_sum.append(items_num[i])

    for i in range(len(items_sum)):
        for j in range(i, len(items_sum)):
            if int(items_sum[i][1]) < int(items_sum[j][1]):
                items_sum[i], items_sum[j] = items_sum[j], items_sum[i]
            if int(items_sum[i][1]) == int(items_sum[j][1]) and items_sum[i][0] > items_sum[j][0]:
                items_sum[i], items_sum[j] = items_sum[j], items_sum[i]

    items_res = []
    for i in range(len(items_sum)):
        n = items_sum[i][0] + " " + items_sum[i][1]
        items_res.append(n)

    return items_res
