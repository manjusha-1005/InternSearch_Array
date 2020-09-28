n=int(input("enter size of array"))
a=[]
for x in range(n):
    b=int(input("enter numbers into array"))
    a.append(b)
a.sort()
m=int(input("enter no.of packets"))
for i in range(n-m+1):
    if i==0:
        min=a[i+m-1]-a[i]
    else:
        b=a[i+m-1]-a[i]
        if b<min:
            min=b
print("minimum difference is",min)
