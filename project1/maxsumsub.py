"""
CS325 - Summer 2015
Project 1
Name: Tingzhi Li, Nicholas Nelson & Chunyang Zhang
Date: 7/9/2015
"""


def enumeration(l):
    n = len(l)
    maximum = l[0]
    start = end = 0

    for i in range(0, n):
        for j in range(i, n):
            summation = 0
            for k in range(i, j):
                if j > i:
                    summation += l[k]
                else:
                    summation = l[i]

            if summation > maximum:
                maximum = summation
                start = i
                end = j

    return dict(subarray=l[start:end], maxsum=maximum)


def better_enumeration(l):
    n = len(l)
    maximum = l[0]
    start = end = 0

    for i in range(0, n):
        summation = 0
        for j in range(i, n):
            summation += l[j]

            if summation > maximum:
                maximum = summation
                start = i
                end = j + 1

    return dict(subarray=l[start:end], maxsum=maximum)


def divide_n_conquer(l):
    n = len(l)
    mid_idx = n/2

    if n == 0:
        return 0
    elif n == 1:
        return max(l[0], 0)

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


# these are just examples for validating that the methods above don't blow up!
b = [31, -41, 59, 26, -53, 58, 97, -93, -23, 84, -1]

print "---enumeration---"
res = enumeration(b)
print "subarray: ", res['subarray']
print "max sum: ", res['maxsum']

print "\n---better_enumeration---"
res = better_enumeration(b)
print "subarray: ", res['subarray']
print "max sum: ", res['maxsum']

print "\n---divide_n_conquer---"
print "max sum: ", divide_n_conquer(b)

print "\n---linear---"
res = linear(b)
print "subarray: ", res['subarray']
print "max sum: ", res['maxsum']