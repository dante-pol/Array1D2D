def sum_1d(list):
    sum = 0

    for e in list:
        sum += e

    return sum
def prod_1d(list):
    prod = 1

    for e in list:
        prod *= e

    return prod
def max_odd_1d(list):
    max = list[0]
    no_odds = True

    for e in list:
        if e % 2 != 0 and max < e:
            max = e
            no_odds = False

    if not no_odds:
        return max