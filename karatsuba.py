def karatsubaMult(x,y) :
    x = str(x)
    y = str(y)
    if len(x) == 1 and len(y) == 1 :
        return int(x) * int(y)

    if len(x) < len(y) :
        x = x.rjust(len(y),"0")

    elif len(y) < len(x) :
        y = y.rjust(len(x),"0")

    n = len(x)
    j = n//2

    #for odd digit int
    if (n%2)!= 0 :
        j += 1

    BZeroPadding = n - j
    AZeroPadding = BZeroPadding * 2
    a = int(x[:j])
    b = int(x[j:])
    c = int(y[:j])
    d = int(y[j:])

    #recursive calculate
    ac = karatsubaMult(a, c)
    bd = karatsubaMult(b, d)
    k = karatsubaMult(a+b, c+d)
    A = int(str(ac).ljust(len(str(ac))+AZeroPadding,"0"))
    B = int(str(k-ac-bd).ljust(len(str(k-ac-bd))+BZeroPadding,"0"))
    return A + B + bd

x = int(input("Enter x:"))
y = int(input("Enter y:"))
print(karatsubaMult(x,y))

