# detect whether two strings with same length are anagrams.

# find-and-delete solution.
def anagramDetection1(a, b):
    # check length equality.
    if len(a) != len(b):
        return False
    # copy string to a list so that element can be adjust.
    bList = list(b)
    for i in a:
        if i not in bList:  # if char in a is not in b, the strings are not anagrams.
            return False
        else:
            bList.pop(bList.index(i))  # find the same char in b, then remove it.
    return True


# sort-then-compare solution.
def anagramDetection2(a, b):
    # check length equality.
    if len(a) != len(b):
        return False
    # sort the list of chars.
    aList = list(a)
    bList = list(b)
    aList.sort()
    bList.sort()
    # compare chars in order.
    for i in range(len(a)):
        if aList[i] != bList[i]:
            return False
    return True


# character-count solution.
def anagramDetection3(a, b):
    # check length equality.
    if len(a) != len(b):
        return False
    # assume strings are composed of ascii code.
    # count and store char occurrence in a list.
    aCount = [0] * 128
    bCount = [0] * 128
    for item in a:
        aCount[ord(item)] = a.count(item)
    for item in b:
        bCount[ord(item)] = b.count(item)
    # compare.
    for (m, n) in zip(aCount, bCount):
        if m != n:
            return False
    return True
