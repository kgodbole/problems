#
# (1) duplicate l1 and check if l2 is substring of l1
# (2) locate index of first element of l2 in l1 and compare elements
# thereafter, wrapping around l1 as may be required
# (3) check for equality, rotate l2, check for equality, further rotate l2 and
# so on
#
def are_equal(l1, l2):
    if len(l1) != len(l2):
        return False

    found = -1
    for i,elem in enumerate(l1):
        if elem != l2[0]:
            continue
        j = i - 1
        k = len(l2) - 1
        while k >= 0:
            if l1[j] != l2[k]:
                break
            j -= 1
            k -= 1
        if k < 0:
            return True
    return False


def check_equal(l1, l2):
    print l1, ",", l2, "are cyclically ", "equal" if are_equal(l1, l2) else "not equal"

def run_test():
    check_equal([1,2,3,4,5], [3,4,5,1,2])
    check_equal([1,1,2,2], [2,1,1,2])
    check_equal([1,1,1,1], [1,1,1,1])
    check_equal([1,1,1], [1,1,1,1])
    check_equal([1,1,1,2], [1,1,1,3])

run_test()
