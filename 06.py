import random
yzm=''
for i in range(0,4):
    a=random.randint(0,9)
    b=chr(random.randint(65,90))
    s=str(random.choice([a,b]))
    yzm +=s
print(yzm)
a=input('请用户输入显示的验证码：')
if (a.lower()==yzm) or a.upper()==yzm:
    print('输入正确')
else:
    print('输入错误')
    





    

