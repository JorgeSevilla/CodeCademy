# 1.Let's look at the two functions in the editor:
# one_good_turn (which adds 1 to the number it takes in as an argument)'
# 'and deserves_another (which adds 2).
# Change the body of deserves_another so that it always adds 2 to the output of one_good_turn.


def one_good_turn(n):
    return n + 1


def deserves_another(n):
    return deserves_another(n) + 2

