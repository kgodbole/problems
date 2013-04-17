valid_moves = [(2,1), (2,-1), (1,-2), (-1,-2), (-2,-1), (-2,1), (-1,2), (1,2)]
paths = None
table = None
revisit_allowed = True


def move(x, y, xend, yend, m, n, path):
    global valid_moves, paths

    if n == 0:
        if x == xend and y == yend:
            paths.append(path)
        return
    elif x == xend and y == yend:
        if not revisit_allowed:
            # reaching in fewer moves is not considered
            return

    for valid_move in valid_moves:
        x1, y1 = x + valid_move[0], y + valid_move[1]
        if x1 < 0 or x1 >= m or y1 < 0 or y1 >= m:
            continue

        if not revisit_allowed:
            if table[x1][y1]:
                continue
                
        table[x1][y1] = True
        move(x1, y1, xend, yend, m, n - 1, path + [(x1, y1)])
        table[x1][y1] = False

def knight_moves(x, y, xend, yend, m, n):
    global paths, table
    paths = []

    table = []
    for i in range(m):
        row = [False for j in range(m)]
        table.append(row)

    move(x, y, xend, yend, m, n, [])
    print "\nNonGen:: (%d, %d) -> (%d, %d) in %d moves is %s" % (x, y, xend, yend, n,
            len(paths) > 0)
    print "Number of paths (revisits allowed is", revisit_allowed,") = ",len(paths)
    #for i,path in enumerate(paths):
    #    print i,":", path


def move_gen(x, y, xend, yend, m, n, path):
    global valid_moves
    follow = False

    if n == 0:
        if x == xend and y == yend:
            yield path
    elif x == xend and y == yend:
        if revisit_allowed:
            follow = True
    else:
        follow = True

    if follow:
        for valid_move in valid_moves:
            x1, y1 = x + valid_move[0], y + valid_move[1]
            if x1 < 0 or x1 >= m or y1 < 0 or y1 >= m:
                continue

            #print "x1:", x1, "y1: ", y1, "m: ",m
            if not revisit_allowed:
                if table[x1][y1]:
                    continue
                    
            table[x1][y1] = True
            for mv in move_gen(x1, y1, xend, yend, m, n - 1, path + [(x1, y1)]):
                yield mv
            table[x1][y1] = False

def knight_moves_using_gen(x, y, xend, yend, m, n):
    global table
    table = []
    for i in range(m):
        row = [False for j in range(m)]
        table.append(row)

    paths = list(move_gen(x, y, xend, yend, m, n, []))
    print "\nGen:: (%d, %d) -> (%d, %d) in %d moves is %s" % (x, y, xend, yend, n,
            len(paths) > 0)
    print "Number of paths (revisits allowed is", revisit_allowed,") = ",len(paths)
    #for i,path in enumerate(paths):
    #    print i,":", path


def crunch():
    global revisit_allowed

    print "\n\nCrunching ...\n"
    for revisit_allowed in [False, True]:
        for i in range(2, 65, 2):
            npaths = 0
            for path in move_gen(0, 0, 7, 7, 8, i, []):
                npaths += 1
            print "\n(",revisit_allowed,",", i,") ->", npaths


knight_moves(0, 0, 0, 0, 8, 0)
knight_moves(0, 0, 0, 0, 8, 1)
knight_moves(0, 0, 0, 0, 8, 2)
knight_moves(0, 0, 2, 1, 8, 1)

knight_moves(0, 0, 2, 0, 8, 1)
knight_moves(0, 0, 2, 0, 8, 2)

knight_moves(0, 0, 1, 0, 8, 1)
knight_moves(0, 0, 1, 0, 8, 2)
knight_moves(0, 0, 1, 0, 8, 3)

revisit_allowed = False
knight_moves(0, 0, 7, 7, 8, 6)
knight_moves_using_gen(0, 0, 7, 7, 8, 6)
revisit_allowed = True
knight_moves(0, 0, 7, 7, 8, 6)
knight_moves_using_gen(0, 0, 7, 7, 8, 6)

revisit_allowed = False
knight_moves(0, 0, 7, 7, 8, 8)
knight_moves_using_gen(0, 0, 7, 7, 8, 8)
revisit_allowed = True
knight_moves(0, 0, 7, 7, 8, 8)
knight_moves_using_gen(0, 0, 7, 7, 8, 8)

#knight_moves(0, 0, 7, 7, 8, 10)
#knight_moves_using_gen(0, 0, 7, 7, 8, 10)

crunch()
