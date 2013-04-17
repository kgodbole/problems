def is_number(elem):
    try:
        float(elem)
        return True
    except ValueError:
        return False

opers = {}
opers["+"] = lambda x,y: x + y
opers["*"] = lambda x,y: x * y
opers["-"] = lambda x,y: x - y
opers["/"] = lambda x,y: x / y
 
def evaluate(expr):
    stack = []
    for elem in expr.split():
        print elem
        if is_number(elem):
            stack.append(elem)
        else:
            elem2 = stack.pop()
            elem1 = stack.pop()
            result = opers[elem](float(elem1), float(elem2))
            stack.append(result)
    print expr," = %.4f" % stack.pop()

evaluate("19 2.14 + 4.5 2 4.3 / - *") 
