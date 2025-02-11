file = open("newfile.txt", "w")
file.write("Hello World")
file.close ()
print ("File Created")

x=0

while x<5:
    file = open("newfile.txt", "r")
    z = (file.read())
    file.close ()
    file = open("newfile.txt", "a")
    file.write(z)
    file.write(str(x))
    file.write("\n")
    file.close ()
    print (x)
    x=x+1
       