"""
CS325 - Summer 2015
Project 1
Name: Tingzhi Li, Nicholas Nelson & Chunyang Zhang
Date: 7/9/2015
"""

import maxsumsub
import random
import time

def main():

    for i in range(10):
        rand_array = random.sample(xrange(-100, 100), 100)
        print (i + 1), ":", rand_array, "\n"

        t0 = time.time()
        maxsumsub.enumeration(rand_array)
        t1 = time.time()
        print "Enumeration:\t\t", (t1 - t0)*1000, "milliseconds (wall time)"

        t0 = time.time()
        maxsumsub.better_enumeration(rand_array)
        t1 = time.time()
        print "Better Enumeration:\t", (t1 - t0)*1000, "milliseconds (wall time)"

        t0 = time.time()
        maxsumsub.divide_n_conquer(rand_array)
        t1 = time.time()
        print "Divide and Conquer:\t", (t1 - t0)*1000, "milliseconds (wall time)"

        t0 = time.time()
        maxsumsub.linear(rand_array)
        t1 = time.time()
        print "Linear-Time:\t\t", (t1 - t0)*1000, "milliseconds (wall time)"
        print "--------------------------------------------"



if __name__ == '__main__':
    main()