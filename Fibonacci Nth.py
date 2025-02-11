x = 0
y = 1
z = 2
a = 10
B = 3
if a < 3:
    print(0)
else:
    if a == 3:
        print(1)
    else:
        while B < a:
            x = y
            y = z
            z = x + y
            B = B + 1
        
        print(z)   