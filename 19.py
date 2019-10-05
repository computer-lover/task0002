a=eval(input('请输入一系列数字：'))
ls1=list(a)
print(ls1)
b=sorted(ls1)
c=list(reversed(b))
print(c)
print(len(c))
k=eval(input('请输入一个k值:'))
if k<=len(c):
    print('第{0}个最大元素是{1}'.format(k,c[k-1]))
while k >len(c):
    k=eval(input('请重新输入k值:'))
    while k<len(c):
        print('第{0}个最大元素是{1}'.format(k,c[k-1]))
        break 
        
        
    
    
       
        
        

    


