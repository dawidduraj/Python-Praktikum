def histogram(strings):
    res = {}
    for string in strings:
        if not (string in res): res[string] = strings.count(string)
    return res

