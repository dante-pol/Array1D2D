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
    