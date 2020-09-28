a=[8,3,1,2]
n=len(a)
sum=0
max=0
for j in range(n):
    k=0
    x=0
    while k<n-1:
        count=0
        a[k],a[x+1]=a[x+1],a[k]
        k=k+1
        x=x+1
        for p in range(n):
            count=count+(a[p]*p)
    print(count)
    if count>max:
        max=count
print(max)
