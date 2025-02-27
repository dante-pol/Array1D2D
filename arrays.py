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