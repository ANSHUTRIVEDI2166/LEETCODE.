def minDominoRotations(tops, bottoms):
    cnta = [0]*7
    cntb = [0]*7
    same = [0]*7
    for t, b in zip(tops, bottoms):
        cnta[t] += 1
        cntb[b] += 1
        if t == b:
            same[t] += 1
    for i in range(1, 7):
        if cnta[i] + cntb[i] - same[i] == len(tops):
            return min(cnta[i], cntb[i]) - same[i]
    return -1
