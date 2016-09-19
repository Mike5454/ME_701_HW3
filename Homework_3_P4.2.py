from __future__ import division

def binary_to_decimal(s):
    if s-int(s) != 0:
        s = str(s)
        i,f = s.split('.')
    else:
        i=str(s)
        f=0
    a = len(str(i))
    b = 1
    d=0
    h=0
    for check in str(i):
        check = int(check)
        e = (check * 2**(a-1))
        d = d + e
        a = a-1
    for check in str(f):
        check = float(check)
        g = (check * (1/pow(2,b)))
        h = h + g
        b = b + 1
    c = (d+h)
    print c

