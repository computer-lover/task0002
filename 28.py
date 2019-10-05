from math import sqrt
m=input('请输入一个正整数：')
n=input('请输入一个正整数：')
t=[]
if m>n:
    m,n=n,m
for i in range(int(m),int(n)):
    a=str(i)
    b=int(a[::-1])
    t.append(b)
t1=[]
for x in iter(t):
    j = 2
    while j <= int(sqrt(x)):
        if x % j == 0:
            break 
        j += 1
    else:
        t1.append(x)
print(t1)


    
    


            
            
            
           
            
        
    
            

            
                
   
                
            
    
  
    

    
    
    

    
    

        
    

   
    
    
    
    
    
        
        
        

    
    

    




