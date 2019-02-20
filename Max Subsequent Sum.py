a=[1,2,34,5,657,78,897,98,4345,2345,32]
sum=sum1=0
for i in range(0,len(a),1):
    if i%2==0:
        sum+=a[i]
    else:
        sum1+=a[i]
if sum>sum1:
    print(sum)
else:
    print(sum1)
