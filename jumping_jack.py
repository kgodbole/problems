#
# first breach the limit enough to prevent divergence
# this reveals one solution yielding an upper limit
# then search for solutions exploring options at each step
# 

# assume target is always positive
def find_nsteps(target):

    # breach
    delta = 1
    n = 0
    jumps = [0]
    while n - delta < target:
        n += delta
        delta += 1
        jumps.append(n)

    if n - delta == target:
        print "Jumps [", delta - 1,"]:", jumps
        return delta-1

    # calculate no. of steps in simple solution
    nsteps = ((n - delta) - target) * 2 + delta
    print "Number of jumps to reach %d = %d" % (target, nsteps)

    # print simple solution just to verify
    flag = -1
    while n != target:
        n += flag * delta
        delta += 1
        flag *= -1
        jumps.append(n)
    print "Jumps [", delta - 1,"]:", jumps
    return nsteps


minsteps = -1

def find_solutions(target, limit):
    find_sols(target, 0, 1, [0], limit)

def find_sols(target, pos, delta, jumps, limit):
    global minsteps

    if delta == limit - 1:
        return
    
    found = False
    newpos = pos + delta
    if newpos == target:
        print "Jumps [", delta, "]:", jumps + [newpos]
        found = True
    else:
        find_sols(target, newpos, delta + 1, jumps + [newpos], limit)

    if found:
        if minsteps == -1:
            minsteps = delta
        elif minsteps > delta:
            minsteps = delta

    found = False
    newpos = pos - delta
    if newpos == target:
        print "Jumps [", delta, "]:", jumps + [newpos]
        found = True
    else:
        find_sols(target, newpos, delta + 1, jumps + [newpos], limit)

    if found:
        if minsteps == -1:
            minsteps = delta
        elif minsteps > delta:
            minsteps = delta


def jj(target):
    global minsteps
    minsteps = -1
    nsteps = find_nsteps(target)
    find_solutions(target, nsteps)
    print "\nMin. no. of steps = %d" % minsteps


jj(12)
