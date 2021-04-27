x = 8
y = 9
i = 1

def num_day(x, y, i):

    while x < y:
        x *= 1.1
        i += 1
    print(i)

num_day(x, y, i)
