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