n=int(input('请输入一个正整数：'))
s=0
for i in range(1,n):
    if i%2==0:
        s=s+i
print(s)
