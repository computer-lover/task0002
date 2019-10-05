N=int(input('请输入一个正整数：'))
s=0
for i in range(1,N):
    if i%3 ==0 or i%5 ==0:
        print(i)
        s=s+i
print(s)
        
