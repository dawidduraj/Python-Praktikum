def isPermutation(list1,list2):
    if len(list1) != len(list2): return False
    
    copy = list2.copy()
    for element in list1:
        if element in copy: copy.remove(element)
        else: return False

    if len(copy) == 0: return True
    else: return False

print(isPermutation([1, 2, 2, 3], [3, 1, 2, 1]))
