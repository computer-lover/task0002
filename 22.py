from time import strftime,gmtime
a=strftime('%Y/%m/%d %H:%M:%S')
ys=int(strftime('%Y'))
if (ys%4==0 and ys%100!=0) or ys%400==0:
    print('{}是闰年!'.format(ys))
else:
    print('{}不是闰年!'.format(ys))
b=[31,28,31,30,31,30,31,31,30,31,30,31]
ms=int(strftime('%m'))
ds=int(strftime('%d'))
s=0
for i in range(1,len(b)):
    if i<ms:
        s=s+b[i]
print(s+ds)

    




