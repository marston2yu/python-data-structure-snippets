# Shell sort for numbers.
# Wrap insertion sort in a loop, the gap is decreased every iteration.

def shellSort(alist):
    # calculate max gap: 1/2(3**k-1)
    gap = 1
    while (gap < len(alist) / 3):
        gap = gap * 3 + 1

    while (gap != 0):
        # insertion sort.
        for i in range(0, len(alist), gap):
            for j in range(i, 0, -gap):
                if alist[j] > alist[j - gap]:
                    break
                else:
                    tmp = alist[j]
                    alist[j] = alist[j - gap]
                    alist[j - gap] = tmp
        # decrease gap.
        gap = gap // 3
    return alist


if __name__ == '__main__':
    print(shellSort([3, 2, 5, 7, 8, 0, 12, 5, 6]))
