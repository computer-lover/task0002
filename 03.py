a=eval(input('请输入a的值：'))
b=eval(input('请输入b的值：'))
c=eval(input('请输入c的值：'))
from math import sqrt
d=b*b-4*a*c
if d>0:
    x1=(-b+sqrt(d))/(2*a)
    x2=(-b-sqrt(d))/(2*a)
    print("方程有两个异根","x1=",x1,"x2=",x2)
elif(d==0):
    x1=x2=-b/2*a
    print("方程有两个同根","x1=x2",x1)
else:
    print('方程无实数解')
