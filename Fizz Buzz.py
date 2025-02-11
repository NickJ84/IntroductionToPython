
i = 1
while i <20:  
    fizz = 0 
    
    if i % 3 ==0:
        fizz = fizz+1
    if i % 5 ==0:
        fizz = fizz+2    
    if fizz == 0 :
        print (i)
    if fizz == 1:
        print (i,'fizz')   
    if fizz == 2:
        print (i,'buzz')    
    if fizz == 3:
        print (i,'fizz buzz')
    
    i = i + 1    