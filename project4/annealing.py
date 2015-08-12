"""
Simulated annealing with restart applied to the traveling salesman problem. 

Based upon the work of Emmanuel Goosaert, with implementation details and 
performance metrics available at: 
http://codecapsule.com/2010/04/06/simulated-annealing-traveling-salesman/

The GPL licensing has been maintained and brought into this work in order to
remain in compliance with the derivative works clauses of the GPLv3 license.
"""
## Copyright (c) 2010 Emmanuel Goossaert 
##
## This file is free software; you can redistribute it and/or modify
## it under the terms of the GNU General Public License as published by
## the Free Software Foundation; either version 3 of the License, or
## (at your option) any later version.
##
## This file is distributed in the hope that it will be useful,
## but WITHOUT ANY WARRANTY; without even the implied warranty of
## MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
## GNU General Public License for more details.
##
## You should have received a copy of the GNU General Public License
## along with this file.  If not, see <http://www.gnu.org/licenses/>.

import math
import random

distances_pair = []

def compute_distance_pairs(cities):
    global distances_pair
    for city_from in cities:
        distances_pair.append([0 for r in range(city_from.index)])
        for city_to in cities[:city_from.index]:
            distances_pair[city_from.index][city_to.index] = city_from.compute_distance(city_to)

def total_distance(cities):
    """Retrieve pre-computed distances to city."""
    distances = [cities[index].distance_to_city(cities[(index + 1) % len(cities)]) for index in range(len(cities))]
    return sum(distances)

class City:

    def __init__(self, index=-1, x=0,  y=0):
        self.index = int(index)
        self.x = int(x)
        self.y = int(y)

    def __str__(self):
        return '%d %d %d' % (self.index, self.x, self.y)

    def __repr__(self):
        return self.__str__()

    def compute_distance(self, city):
        x = pow((self.x - city.x), 2)
        y = pow((self.y - city.y), 2)
        return round(math.sqrt(x + y))

    def distance_to_city(self, city):
        global distances_pair
        if self.index != city.index:
            indices = [self.index, city.index]
            return distances_pair[max(indices)][min(indices)]
        return 0

def compute_swap_indices(index, nb_cities):
    index_previous = (index - 1 + nb_cities) % nb_cities
    index_next = (index + 1) % nb_cities
    return (index_previous, index_next)

def distance_swap(cities, index_a, index_b):
    """Compute the distance inferred by the two given indices."""
    index_A = min(index_a, index_b)
    index_B = max(index_a, index_b)
    
    (index_A_previous, index_A_next) = compute_swap_indices(index_A, len(cities))
    (index_B_previous, index_B_next) = compute_swap_indices(index_B, len(cities))
  
    distances = []
    # These two distances are common to the two sub-cases
    distances.append(cities[index_A_previous].distance_to_city(cities[index_A]))
    distances.append(cities[index_B].distance_to_city(cities[index_B_next]))
    if index_A == index_B_previous:
        # B is following A in the list: the distance between A and B must not
        # be counted twice.
        # ---x---A---B---x---
        distances.append(cities[index_A].distance_to_city(cities[index_B]))
    else:
        # B is not following A in the list: all distances must be counted
        # ---x---A---x--- ... ---x---B---x---
        distances.append(cities[index_A].distance_to_city(cities[index_A_next]))
        distances.append(cities[index_B_previous].distance_to_city(cities[index_B]))

    return sum(distances)

def annealing(cities, temperature_begin=1.0e+300, temperature_end=.1, cooling_factor=.99, nb_iterations=1):
    """
    Simulated annealing function, developed by Emmanuel Goossaert and
    implemented with acceptance probability from Kirkpatrick et al., and 
    with restart.

    distance_best:    best solution encountered so far
    distance_current: solution used in the current simulation
    distance_new:     solution computed from the random changes to current
    """
    count = 0

    cities_best = cities[:]
    distance_best = total_distance(cities_best)

    distances_current = []
    distances_best = []
    ids_iteration = []

    try:
        for iteration in range(nb_iterations):
            # the search is restarted at every iteration from
            # the best know solution
            temperature = temperature_begin
            cities_current = cities_best[:]
            distance_current = distance_best
            distance_new = distance_best
            cities_new = cities_best[:]

            step = 0
            while temperature > temperature_end:
                count = count + 1
                print 'count: %d' % count
                # compute the indices of the two cities to swap by random,
                # but never touch the first city (it does not need to change)
                index = random.sample(range(len(cities_new) - 1), 2)
                index[0] += 1
                index[1] += 1

                # optimize by recomputing only the changed distances
                swap_before = distance_swap(cities_new, index[0], index[1])
                cities_new[index[0]], cities_new[index[1]] = cities_new[index[1]], cities_new[index[0]]
                swap_after = distance_swap(cities_new, index[0], index[1])

                # compute the new distance
                # recomputing all is bad: distance_new = total_distance(cities_new)
                distance_new = distance_new - swap_before + swap_after

                # acceptance probability by Kirkpatrick et al.
                diff = distance_new - distance_current
                if diff < 0 or  math.exp( -diff / temperature ) > random.random():
                    cities_current = cities_new[:]
                    distance_current = distance_new
                else:
                    # reset cities and distance
                    distance_new = distance_current
                    cities_new = cities_current[:]

                # update the best if current solution is better
                # not part of the annealing itself, just used for the restart
                if distance_current < distance_best:
                    cities_best = cities_current[:]
                    distance_best = distance_current

                if True:
                    # if step % 100 == 0:
                    # uncomment to enable systematic sampling: 1 point every 100th
                    distances_current.append(distance_current)
                    distances_best.append(distance_best)
                temperature = temperature * cooling_factor
                step = step + 1

            ids_iteration.append(len(distances_current))

    except KeyboardInterrupt, e:
        print "Interrupted on user demand."
        print 'performed iterations: %d' % interation

    return cities_best, distances_current, distances_best, ids_iteration