a = 1504

def year1(year):

    if (year % 4 == 0) and (year % 100 != 0) or (year % 400 == 0):
        print("yes")
    else:
        print('no')

year1(a)
