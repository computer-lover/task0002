from datetime import datetime
a=input('请用户输入身份证号：')
now=datetime.now()
print(now.year)
print('该用户的出生年月日是{}'.format(a[6:14]))
print('该用户的年龄是{}'.format(now.year-int(a[6:10])))
if int(a[16])%2==0:
    print('该用户为女性')
else:
    print('该用户为男性')

