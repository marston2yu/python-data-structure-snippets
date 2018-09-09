# Quick sort.

def quickSort(alist):
    quickSortHelper(alist, 0, len(alist) - 1)


def quickSortHelper(alist, first, last):
    # recursion ending flag.
    if first >= last:
        return
    # partition makes all value to the left of split point smaller than value of the split point, right vice versa.
    splitPoint = partition(alist, first, last)
    quickSortHelper(alist, first, splitPoint - 1)
    quickSortHelper(alist, splitPoint + 1, last)


def partition(alist, first, last):
    leftmark = first + 1
    rightmark = last
    pivotValue = alist[first]
    found = False
    while not found:
        # increase left mark until find the value bigger than pivot value.
        while leftmark <= rightmark and alist[leftmark] <= pivotValue:
            leftmark = leftmark + 1
        # decrease right mark until find the value smaller than pivot value.
        while leftmark <= rightmark and alist[rightmark] >= pivotValue:
            rightmark = rightmark - 1

        # if the left mark and right mark don't cross, swap the values they point to.
        if leftmark > rightmark:
            found = True
        else:
            tmp = alist[leftmark]
            alist[leftmark] = alist[rightmark]
            alist[rightmark] = tmp

    # finally, swap pivot value, i.e, the first value, with the value that right mark point to.
    tmp = alist[rightmark]
    alist[rightmark] = alist[first]
    alist[first] = tmp

    return rightmark


if __name__ == '__main__':
    alist = [3, 2, 5, 7, 8, 0, 12, 5, 6]
    quickSort(alist)
    print(alist)
