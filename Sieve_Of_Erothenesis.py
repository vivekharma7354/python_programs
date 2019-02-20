a=int(input("Please Enter Upper Range For Prime :- "))
prime=[True for _ in range(a+1)]
p=2
while(p<a):
    if (prime[p]==True):
        for k in range(p+p,a+1,p):
            prime[k]=False
    p+=1
for i in range(2,a+1):
    if prime[i]==True:
        print(i)
