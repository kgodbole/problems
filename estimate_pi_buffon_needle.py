import random
import math

#
# number of lines is 'm'
# drop needle 'n' times
# count how many 'nint' interesect a line
# pi = 2 * n / nint if only acute angles are chosen randomly
#

def drop_needle(m):
    # pick a point for head of the needle randomly
    y1 = random.uniform(0, m - 1)

    # pick an angle of rotation randomly
    #theta = random.uniform(0, 360.0)
    theta = random.uniform(0, 90.0)

    # find other end of needle
    y2 = y1 + math.sin(math.radians(theta))

    # if intersects, return True
    if int(y1) - int(y2) != 0:
        return True
    return False


def calculate_pi(m, n):
    nint = 0
    for i in xrange(n):
        if drop_needle(m):
            nint += 1
    print "[1](%d, %d): pi = %f" % (m, n, 2.0 * float(n) / nint)


def drop_needle2(m):
    # pick a point for head of the needle randomly
    y1 = random.uniform(0, m - 1)

    # pick an angle of rotation randomly
    #theta = random.uniform(0, 90.0)
    theta = random.uniform(0, 360.0)

    rem = theta % 90.0
    quadrant = int(theta / 90.0)
    sign = 1 + (quadrant / 2) * -2
    theta1 = (quadrant % 2) * (90.0 - rem) + ((quadrant + 1) % 2) * rem
    y2 = y1 + sign * math.sin(math.radians(theta1))
    #print "y1 = %f, theta = %f, y2 = %f, rem = %f, quadrant = %d, sign = %d,\
            #    theta1 = %f" % (y1, theta, y2, rem, quadrant, sign, theta1)

    # if intersects, return True
    if int(y1) - int(y2) != 0:
        return True
    return False


def calculate_pi2(m, n):
    nint = 0
    for i in xrange(n):
        if drop_needle2(m):
            nint += 1
    print "[2](%d, %d): pi = %f" % (m, n, float(n) / nint)


def play_around():
    calculate_pi(2, 100)
    calculate_pi(3, 100)
    calculate_pi(2, 100000)
    calculate_pi(2, 1000000)
    calculate_pi(3, 1000000)
    calculate_pi(3, 10000000)
    calculate_pi(10, 1000000)
    calculate_pi(10, 10000000)

    calculate_pi2(2, 100)
    calculate_pi2(3, 100)
    calculate_pi2(2, 100000)
    calculate_pi2(2, 1000000)
    calculate_pi2(3, 1000000)
    calculate_pi2(3, 10000000)
    calculate_pi2(10, 1000000)
    calculate_pi2(10, 10000000)

play_around()
