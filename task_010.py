def BigMinus(s1, s2):
    if s1 == s2:
        return 0

    if len(s1) < len(s2):
        s1, s2 = s2, s1

    if len(s1) == len(s2):
        for i in range(len(s1)):
            if s1[i] > s2[i]:
                break
            else:
                s1, s2 = s2, s1
                break

    arr1 = list(s1)
    arr2 = list(s2)

    arr1.reverse()
    arr2.reverse()

    if len(s1) != len(s2):
        for i in range(len(s2), len(s1)):
            arr2.append("0")

    arr = []
    n = 0
    for i in range(len(arr1)):
        if int(arr1[i]) + n - int(arr2[i]) < 0:
            a = int(arr1[i]) + 10 + n - int(arr2[i])
            arr.append(str(a))
            n = -1
        else:
            arr.append(str(int(arr1[i]) + n - int(arr2[i])))
            n = 0

    arr.reverse()

    if arr[1] == 0:
        for i in range(len(arr)):
            while arr[i] == 0:
                del arr[i]


    return "".join(arr)



