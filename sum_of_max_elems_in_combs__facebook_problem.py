import types

def fact(n):
    if n == 0:
        return 1
    return n * fact(n-1)

def comb(n, r):
    return fact(n)/(fact(n-r) * fact(r))

def find_sum(l, k):
    print "\nFinding sum for list ",l," and k = ",k
    n = len(l)
    total = 0
    l.sort()
    for i in range(k-1, n):
        total += comb(i, k-1) * l[i]
        if total >= 1000000007:
            total = total % 1000000007
    print "Total =",total

def run_test():
    find_sum([3,6,2,8], 3)
    find_sum([10,20,30,40,50], 2)
    find_sum([0,1,2,3,5,8], 4)
    find_sum([1069,1122], 2)
    find_sum([10386,10257,10432,10087,10381,10035,10167,10206,10347,10088], 5)

run_test()


def fact_gen(n, total):
    if n == 0:
        yield total
    else:
        yield fact_gen(n - 1, n * total)

def run_gen(gen, *args):
    print "\nRunning generator ",gen," with args ",args
    g = gen(*args)
    l = [g]
    while l:
        g = l.pop()
        g = g.next()
        if isinstance(g, types.GeneratorType):
            l.append(g)
        else:
            print g
    print "Done"

run_gen(fact_gen, 4, 1)
