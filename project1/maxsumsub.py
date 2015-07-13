"""
CS325 - Summer 2015
Project 1
Name: Tingzhi Li, Nicholas Nelson & Chunyang Zhang
Date: 7/12/2015
"""

import sys
import re
import ast


def main():
    file_name = sys.argv[1]
    fp = open(file_name)
    contents = fp.read()
    fp.close()
    arrays = [ast.literal_eval(l) for l in re.findall(r'\[.*\]', contents)]

    for count, array in enumerate(arrays):
        print (count + 1), ":", array, "\n"

        res = enumeration(array)
        print "Enumeration:\t\t", res['subarray'], ", sum:", res['maxsum']

        res = better_enumeration(array)
        print "Better Enumeration:\t", res['subarray'], ", sum:", res['maxsum']

        print "Divide and Conquer:\t", "sum:", divide_n_conquer(array)

        res = linear(array)
        print "Linear-Time:\t\t", res['subarray'], ", sum:", res['maxsum'], "\n"
        print "--------------------------------------------"

def enumeration(l):
    if not l:   # list is empty
        return dict(subarray=l, maxsum="none")

    maxsum = start = end = 0
    n = len(l)
    for i in range(0, n):
        for j in range(i, n):
            ksum = sum(l[i:j+1])

            if ksum > maxsum:
                maxsum = ksum
                start = i
                end = j + 1

    return dict(subarray=l[start:end], maxsum=maxsum)


def better_enumeration(l):
    if not l:   # list is empty
        return dict(subarray=l, maxsum="none")

    maxsum = l[0]
    start = 0
    end = 1
    n = len(l)
    for i in range(0, n):
        ksum = 0
        for j in range(i, n):
            ksum += l[j]

            if ksum > maxsum:
                maxsum = ksum
                start = i
                end = j + 1

    return dict(subarray=l[start:end], maxsum=maxsum)


def divide_n_conquer(l):
    n = len(l)
    mid_idx = n/2

    if n == 0:
        return 0
    elif n == 1:
        return l[0]

    left = divide_n_conquer(l[:mid_idx])
    right = divide_n_conquer(l[mid_idx:])

    left_half = right_half = 0

    # left-side evaluation
    accum = 0
    for x in l[mid_idx-1::-1]:
        accum += x
        left_half = max(left_half, accum)

    # right-side evaluation
    accum = 0
    for x in l[mid_idx:]:
        accum += x
        right_half = max(right_half, accum)

    return max(left, right, left_half + right_half)


def linear(l):
    best = cur = cur_idx = start = end = 0

    for i, val in enumerate(l):
        if cur + val > 0:
            cur += val
        else:
            cur = 0
            cur_idx = i + 1

        if cur > best:
            start = cur_idx
            end = i + 1
            best = cur

    return dict(subarray=l[start:end], maxsum=best)


if __name__ == '__main__':
    main()
