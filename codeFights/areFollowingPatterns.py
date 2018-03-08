from collections import defaultdict
def areFollowingPatterns(strings, patterns):
    d1, d2 = defaultdict(list), defaultdict(list)
    for i, e in enumerate(strings):
        d1[e].append(i) 
    for j, p in enumerate(patterns):
        d2[p].append(j)
    for i in range(len(strings)):
        if d1[strings[i]] != d2[patterns[i]]:
            return False
    return True 
