T=input('请输入带有符号的温度值：')
while T[-1] not in ['F','f'] or ['C','c']:
    if T[-1] in ['F','f']:
        C=(eval(T[0:-1])-32)/1.8
        print('转化后的温度是{:.2f}C'.format(C))
    elif T[-1] in ['C','c']:
        F=1.8*eval(T[0:-1])+32
        print('转化后的温度是{:.2f}F'.format(F))
    else:
        print('输入格式错误')
    T=input('重新输入带有符号的温度值：')
    

        
        

