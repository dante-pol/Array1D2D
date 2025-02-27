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

def max_among_odd_numbers(array):

    max = array[0]

    for number in array:
        if number > max:
            max = number

"""
МИН СРЕДИ НЕЧЕТНЫХ
РЕВЕРС
ЧТО ХОЧУ
"""

def min_among_odd(array):
    if(len(array) == 1 and array[0] % 2 == 0):
        return -1
    elif(len(array) == 1):
        return array[0]
    
    min = array[0]
    if(array[0] % 2 == 0):
        for i in range(1, len(array)):
            if(array[i] % 2 != 0):
                min = array[i]
                break

    for i in range(1, len(array)):
        if(min > array[i] and array[i] % 2 != 0):
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

def summ(array):
    summ = 0
    for i in range(len(array)):
        summ += array[i]
    return summ

def proiz(array):
    proiz_elem = 1
    for i in range(len(array)):
        proiz_elem *= array[i]
    return proiz_elem

def sum(a):
    sum=0
    for i in a:
        sum+=a[i]
    return sum

def proz(a):
    proz=1
    for i in a[i]:
        proz*=a[i]
    return proz

def max(a):
    max=a[0]
    for i in a:
        if max<a[i]:
            max=a[i]
    return max