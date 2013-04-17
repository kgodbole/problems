ops = "+*N"

def solve(n, numbers):
    operands = []
    operators = []
    print "calling solve1 ..."
    solve1(n, numbers, operands, operators)

def solve1(n, numbers, operands, operators):
    global ops

    if len(numbers) == 1:
        nopd = []
        nopr = []
        topd = operands[:]
        topd.append(numbers[0])
        topr = operators[:]
        topr.append(" ")

        print 40 * '='
        print zip(operands, operators)
        print zip(topd, topr)
        print 40 * '-'

        # firstly, eliminate N that represents No operator
        temp = topd[0]
        lastop = topr[0]
        for index, (operand, operator) in enumerate(zip(topd[1:], topr[1:])):
            consumed = False
            if lastop == "N":
                temp += operand
                consumed = True
                if operator == "N":
                    continue
            if consumed:
                lastop = operator
                continue
            nopd.append(int(temp))
            nopr.append(lastop)
            temp = operand
            lastop = operator
            if index == len(topd[1:]) - 1 and not consumed:
                nopd.append(int(temp))
                nopr.append(lastop)

        print zip(nopd, nopr)
        topd = nopd
        topr = nopr
        nopd = []
        nopr = []

        # secondly, eliminate "*" operator
        temp = topd[0]
        lastop = topr[0]
        for index, (operand, operator) in enumerate(zip(topd[1:], topr[1:])):
            consumed = False
            if lastop == "*":
                temp *= int(operand)
                consumed = True
                if operator == "*":
                    continue
            if consumed:
                if index != len(topd[1:]) - 1:
                    lastop = operator
                    continue
            nopd.append(int(temp))
            nopr.append(lastop)
            temp = operand
            lastop = operator

        print zip(nopd, nopr)

        # finally, eliminate "+" operator
        total = sum(nopd)

        print zip(operands,operators), "total = ", total
        if total != n:
            return

        print "FOUND ::", operands, operators, "total = ", total
        return

    for op in ops:
        operands.append(numbers[0])
        operators.append(op)
        solve1(n, numbers[1:], operands,
                operators)
        operands.pop()
        operators.pop()

solve(2001, "123456789")
