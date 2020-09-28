n=int(input("enter number"))
a=[]
for x in range(n):
    b=int(input("enter numbers into array"))
    a.append(b)
for i in range(0,n-1,2):
    if a[i]>a[i+1]:
        a[i],a[i+1]=a[i+1],a[i]
for j in range(1,n-1,2):
    if a[j]<a[j+1]:
        a[j],a[j+1]=a[j+1],a[j]
print(a)
