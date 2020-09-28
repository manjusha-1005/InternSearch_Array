n=int(input("enter range"))
k=int(input("enter difference"))
a=[]
for x in range(n):
    b=int(input("enter numbers into array"))
    a.append(b)
a.sort()
j=n-1
for i in range(0,n-1,1):
    while i<j:
        if a[j]-a[i]>k:
              j=j-1
        elif a[j]-a[i]<k:
            i=i+1
        else:
            print(a[i],a[j])
            j=j-1
    j=n-1
