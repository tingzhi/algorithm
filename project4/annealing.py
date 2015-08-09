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


distances_pair = []

def compute_distance_pairs(cities):
    global distances_pair
    for city_from in cities:
        distances_pair.append([0 for r in range(city_from.index)])
        for city_to in cities[:city_from.index]:
            distances_pair[city_from.index][city_to.index] = city_from.compute_distance(city_to)

def total_distance(cities):
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