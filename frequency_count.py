a="hello world python"
h=[]
str=''
for i in a:
    num=a.count(i)
    if i in str:
        h.append(None)
    else:
        h.append(num)
        str+=i
print('string',list(a))
print('list',h)
