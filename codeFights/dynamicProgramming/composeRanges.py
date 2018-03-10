def composeRanges(arr):
    if not arr:
        return []
    res = [[arr[0]]]
    for n in arr[1:]:
        if n == (res[-1][-1]+1):
            res[-1].append(n)
        else:
            res.append([n])
    final = []
    for e in res:
        if len(e) > 1:
            final.append(str(e[0])+'->'+str(e[-1]))
        else:
            final.append(str(e[0]))
    return final
