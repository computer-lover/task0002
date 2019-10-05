import random
a=random.randint(1,100)
print(a)
b=eval(input('请用户输入一个（1,100）之间的数：'))
count=1
if a==b:
    print('恭喜您，猜对了')
while a!=b:
    if b<a:
        print('偏小')
    else:
        print('偏大')
    b=eval(input('请用户再输入一个（1,100）之间的数：'))
    count=count+1
    if count==7 and a!=b:
        print('对不起，您猜错了')
        break
    
        
    
         
    


    
        
       
   
    
        
        
    
    
