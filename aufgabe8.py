def histogram(lists):
    sets = [frozenset(sublist) for sublist in lists]
    res = {}
    for set in sets:
        if not (set in res): res[set] = sets.count(set)
    return res
