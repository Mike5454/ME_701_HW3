from __future__ import division

def decimal_to_binary(x, n):
    a=int(x)
    b=x-a
    pl=1
    big=0
    small=0
    while a !=0 :
        dig = a % 2
        val = dig *pl
        pl=pl*10
        big = big+val
        a=int(a/2)
    pl=0.1
    for n in range (1,n+1):
        op=(1/(2**n))
        if b-op >=0:
            dig = 1
        else:
            dig = 0
        val = dig *pl
        pl=pl/10
        small = small + (val*dig)
        b = b-(op*dig)
    fin=big+small
    return (fin)