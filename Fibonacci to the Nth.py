
x = 8

a = 0
b = 1
c = 1

if x == 1:
    print (a)
elif x==2:
    print (b)
elif x==3:
    print (c)
elif x>3:
    while x>3:
        a = b
        b = c
        c = a+b
        x = x-1
print (c)        