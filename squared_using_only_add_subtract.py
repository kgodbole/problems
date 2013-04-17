def find_squared(n, niter):
    if niter == 0:
        return 0

    total = n
    count = 1
    while count + count <= niter:
        total += total
        count += count

    rem = niter - count
    return total + find_squared(n, rem)


def find_squared_faster(n, total, count):
    if count + count > n:
        return n - count, total
    n1, total1 = find_squared_faster(n, total + total, count + count)
    if count > n1:
        return n1, total1
    return n1 - count, total1 + total


def squared(n):
    nsq = find_squared(n, n)
    nleft, nsq1 = find_squared_faster(n, n, 1)
    print "%d squared = %d, %d squared faster = %d" % (n, nsq, n, nsq1)

def test_squared():
    for i in xrange(32):
        squared(i)

test_squared()
