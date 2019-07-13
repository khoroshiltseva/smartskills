def WordSearch(n, s, subs):
    word = s.split(" ")

    strings = []
    current = ""

    for i in range(len(word)):
        if current == "" and len(word[i]) <= n:
            current = str(word[i])
        elif current == "" and len(word[i]) > n:
            current = str(word[i][:n])
            c.append("".join(current))
            current = ""
            word[i] = word[i][n:]
            for j in range((len(word[i]) // n) + 1):
                if len(current) == n:
                    strings.append("".join(current))
                current = str(word[i][:n])
                word[i] = word[i][n:]
                if len(word[i]) == 0:
                    break
        elif current != "" and len(current) + len(word[i]) + 1 <= n:
            current += " "
            current += str((word[i]))
        elif current != "" and len(word[i]) >= n:
            current += " "
            current += str(word[i][:(n - len(current))])
            strings.append("".join(current))
            word[i] = word[i][(n - len(current)):]
            current = ""
            for j in range((len(word[i]) // n) + 1):
                if len(current) == n:
                    strings.append("".join(current))
                current = str(word[i][:n])
                word[i] = word[i][n:]
                if len(word[i]) == 0:
                    break
        else:
            strings.append("".join(current))
            current = str(word[i])

    strings.append("".join(current))

    result = []
    for i in range(len(strings)):
        words = strings[i].split(" ")
        if subs in words:
            result.append(1)
        else:
            result.append(0)

    return result




