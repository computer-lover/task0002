n = input("请以列表格式输入一个列表：\n")
ls = list(n[1:-1].split(","))
ls = list(map(int,ls)) 
lt = []
print(ls)
num = 1
for i in range(len(ls)):
    for j in range(len(ls)):
        num = num * ls[j]
    num = num / ls[i]
    lt.append(num)
    num =1
print(lt)

