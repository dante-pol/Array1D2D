def prod_of_elements_more_three(array):

    sum = 1

    for number in array:
        if number > 3:
            sum *= number

    return sum