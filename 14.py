a=eval(input('请输入一个数：'))
b=eval(input('请输入一个数：'))
c=eval(input('请输入一个数：'))
if a<c:
    a,c=c,a
elif a<b:
    a,b=b,a
print(a)
