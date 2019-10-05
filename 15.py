ys=int(input('请用户输入一个年份：'))
if (ys%4==0 and ys%100!=0) or ys%400==0:
    print('{}是闰年!'.format(ys))
else:
    print('{}不是闰年!'.format(ys))
    

