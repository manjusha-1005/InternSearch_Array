a=[1,0,1,1,1,0,0]
n=len(a)
b=0
c=0
x=0
y=0
max=0
for i in range(0,n-1,1):
    for j in range(i,n,1):
        if a[j]==0:
            b=b+1
        if a[j]==1:
            c=c+1
    if b==c:
        z=j-i
        if z>max:
            max=z
            x=i
            y=j
    else:
        b=0
        c=0
i=i+1
if max==0:
    print("no such array")
else:
    print(x,y)
            
 
