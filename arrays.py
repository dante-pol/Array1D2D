def summ(array):
    summ = 0
    for i in range(len(array)):
        summ += array[i]
    return summ

def maxi(array):
    maxi_elem=array[0]
    for i in range(len(array)):
        if maxi_elem<array[i]:
            maxi_elem=array[i]
    return maxi_elem


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