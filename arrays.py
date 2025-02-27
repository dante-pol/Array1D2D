def prod_of_elements_more_three(array):

    sum = 1

    for number in array:
        if number > 3:
            sum *= number

    return sum

def prod_among_odd_numbers(array):

    sum = 1

    for number in array:
        if number % 2 != 0:
            sum *= number

    return sum