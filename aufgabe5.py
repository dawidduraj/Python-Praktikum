def statistics(data):
    stats = {}
    sort = sorted(data)
    mean = sum(sort) / len(sort)

    variance = 0
    for num in data:
        variance += (num - mean)**2
    
    median = 0
    mid = (len(sort) - 1) // 2
    if (len(sort) % 2):
        median = sort[mid]
    else:
        median = (sort[mid] + sort[mid+1]) / 2.0
    
    stats["mean"] = mean
    stats["variance"] = variance / len(sort)
    stats["median"] = median
    stats["maximum"] = sort[-1]
    stats["minimum"] = sort[0]
    return stats

