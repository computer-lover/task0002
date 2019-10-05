a=input('请用户输入一个字符串：')
letters=0
numbers=0
others=0
for i in a:
    if i.isdigit():
        numbers+=1
    elif i.isalpha():
        letters+=1
    else:
        others+=1
print('英文字母有{}个，数字字符有{}个，其他字符有{}个！'.format(letters,numbers,others))
        
