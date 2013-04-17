def primes(n):
    l = [i for i in range(3, n+1, 2)]
    l.insert(0, 2)

    # sift away
    for i in xrange(1, len(l)):
        if l[i] * l[i] >= n:
            break
        delinds = []
        for j in xrange(i + 1, len(l)):
            if l[j] % l[i] == 0:
                delinds.append(j)
        for i,delind in enumerate(delinds):
            l.pop(delind - i)

    print "Number of primes <= %d is %d" % (n, len(l))


def test_primes():
    primes(10)
    primes(13)
    primes(100)
    #primes(15485863)

test_primes()
