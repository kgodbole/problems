import random
import sys

# card is represented column-wise
def gen_bingo_card():
    card = []
    start = 1
    stop = 15
    for i in xrange(5):
        col = [random.randint(start, stop) for i in xrange(5)]
        card.append(col)
        start += 15
        stop += 15
    return card

def print_card(card):
    for i in xrange(5):
        for j in xrange(5):
            sys.stdout.write(str(card[j][i]) + " ")
        print

def call_out(card):
    pass

def run_game(n):
    card = gen_bingo_card()
    print_card(card)

run_game(10)
