def sum (a,b,*c):
    print(type (c))
    print(c)
    sum=a+b
    for i in c:
        sum =sum +i
        return sum