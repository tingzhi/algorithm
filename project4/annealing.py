import math

distances_pairs = []

def compute_distance(x1, x2, y1, y2):
    x = pow((int(x1)-int(x2)),2)
    y = pow((int(y1)-int(y2)),2)
    sqr = math.sqrt(x+y)
    print "sqrt:", sqr,
    print "round:", round(sqr)