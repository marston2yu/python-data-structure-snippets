# Merge sort. Top-down version and bottom-up version.
import numpy as np


def merge(alist, lo, mid, hi):
    i = lo
    j = mid + 1
    auxiliaryList = list(alist)
    for k in range(lo, hi + 1):
        if j > hi:
            alist[k] = auxiliaryList[i]
            i = i + 1
        elif i > mid:
            alist[k] = auxiliaryList[j]
            j = j + 1
        elif auxiliaryList[i] < auxiliaryList[j]:
            alist[k] = auxiliaryList[i]
            i = i + 1
        else:
            alist[k] = auxiliaryList[j]
            j = j + 1


# Top-down version.
def tdMerge(alist, lo, hi):
    if lo >= hi:
        return
    mid = (lo + hi) // 2

    tdMerge(alist, lo, mid)
    tdMerge(alist, mid + 1, hi)
    merge(alist, lo, mid, hi)
    return alist


def tdMergeSort(alist):
    tdMerge(alist, 0, len(alist) - 1)


# Bottom-up version.
def buMergeSort(alist):
    size = 1  # Merge from size * 2 = 2.
    while size < len(alist):
        for lo in range(0, len(alist) - size, size * 2):
            # Low limit is increased by 2*size so that
            # mid = lo + size, hi = lo + size * 2
            # hi must be smaller than array range, witch is `len(alist) - 1`
            # minus 1 result from difference between size and index.
            merge(alist, lo, lo + size - 1, np.min([len(alist) - 1, lo + 2 * size - 1]))
        size = size * 2  # Double the size.


if __name__ == '__main__':
    alist = [3, 2, 5, 7, 8, 0, 12, 5, 6]
    tdMergeSort(alist)
    print(alist)

    blist = [3, 2, 5, 7, 8, 0, 12, 5, 6]
    buMergeSort(blist)
    print(blist)
