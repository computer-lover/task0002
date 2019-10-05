a=input('请用户输入一个字符串：')
b=input('请用户输入指定的字符：')
c=[]
s=0
l=len(a)
while s<l:
    t=a.find(b,0,l)
    c.append(t)
    s=t+1
    while s>l:
        print(c)
        break




        
    



    

