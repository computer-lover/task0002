for i in range(100,1000):
    a=i//100
    b=i%100//10
    c=i%10
    if a**3+b**3+c**3==i:
        t.append(i)
t1=list(map(str,t))
print(','.join(t1))

        
  
        
        
        
        
   
        
