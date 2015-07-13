"""
CS325 - Summer 2015
Project 1
Name: Tingzhi Li, Nicholas Nelson & Chunyang Zhang
Date: 7/12/2015
"""

import maxsumsub
import random
import time
import datetime
import csv

def main():
    array_size = [100, 200, 300, 400, 500, 600, 900, 1000, 2000, 3000, 4000, 5000]
    file_name = "project1.csv"

    with open(file_name, 'wb') as csvfile:
        writer = csv.writer(csvfile, delimiter=",", quotechar="'", quoting=csv.QUOTE_MINIMAL)
        writer.writerow(['size'] + ['set'] + ['algorithm'] + ['timing'])

        for size in array_size:

            for i in range(10):
                rand_array = [random.randint(-100,100) for x in range(0, size)]
                print "size:", len(rand_array), ", set:", (i + 1)

                t0 = time.time()
                maxsumsub.enumeration(rand_array)
                t1 = time.time()
                writer.writerow([size] + [(i + 1)] + ['enumeration'] + [(t1 - t0)*1000])

                t0 = time.time()
                maxsumsub.better_enumeration(rand_array)
                t1 = time.time()
                writer.writerow([size] + [(i + 1)] + ['better_enumeration'] + [(t1 - t0)*1000])

                t0 = time.time()
                maxsumsub.divide_n_conquer(rand_array)
                t1 = time.time()
                writer.writerow([size] + [(i + 1)] + ['divide_n_conquer'] + [(t1 - t0)*1000])

                t0 = time.time()
                maxsumsub.linear(rand_array)
                t1 = time.time()
                writer.writerow([size] + [(i + 1)] + ['linear_time'] + [(t1 - t0)*1000])

    print "Successfully written to file:", file_name


if __name__ == '__main__':
    main()
