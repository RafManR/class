a = 1
b = 1
c = 8
d = 8


def king_move(a, b, c, d):
    if a == c - 1 and b == d - 1:
        print('yes')
    else:
        print('no')

king_move(a, b, c, d)