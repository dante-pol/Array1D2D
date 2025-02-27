"""
МИН СРЕДИ НЕЧЕТНЫХ
РЕВЕРС
ЧТО ХОЧУ
"""

def min_among_odd(array):
    if(len(array) == 1 and array[0] % 2 != 0):
        return -1
    elif(len(array) == 1):
        return array[0]
    
    min = array[0]
    if(array[0] % 2 != 0):
        for i in range(1, len(array)):
            if(array[i] % 2 == 0):
                min = array[i]
                break

    for i in range(1, len(array)):
        if(min > array[i] and array[i] % 2 == 0):
            min = array[i]

    return min


def reverse(array):
    for i in range(0, len(array) // 2):
        temp = array[len(array) - i - 1]
        array[len(array) - i - 1] = array[i]
        array[i] = temp

def sum_odd(array):
    sum = 0
    
    for el in array:
        if(el % 2 != 0):
            sum += el

    return sum