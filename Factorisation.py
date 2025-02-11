
x = 360

a = 1
B = 0
list = []

while a < x:
    B=x/a
    if B.is_integer():
        list.append(B)
    a = a + 1
print(list)
print("there are",len(list) ,"factors of x")
