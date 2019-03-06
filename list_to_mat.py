def mat_make(A,r,c):
    b=[[] for _ in range(r)]
    if len(A)>=r*c:
        f=0
        co=1
        for k in A:
            if co==c:
                co=1
                fg +=1
            b.append(k)
            co+=1
        return b
    else:
        print('Insufficient Data In List')
a=[1,2,3,4,5,6,7,8,5,4,3,5]
re,ce=eval(input())
print(mat_make(a,re,ce))
