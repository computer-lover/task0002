a=1
b=1
n=int(input())
if n<2:
    print(1)
else:
    for i in range(1,n):
        a,b=b,a+b
    print(b,end=' ')
    
