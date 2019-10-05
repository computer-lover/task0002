n=eval(input('请输入一个正整数：'))
t=1
a=[]
total=0
for u in range(1,n+1):
    t=t*u
    print(t)
    a.append(t)
print(a)
for i in range(0,len(a)):
    total=total+a[i]
print(total)
    
    



    

        
