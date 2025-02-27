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

