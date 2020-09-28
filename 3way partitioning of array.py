a=[1,14,5,20,4,2,54,20,87,98,3,1,32]
lv=int(input("enter low value"))
hv=int(input("enter high value"))
n=len(a)
i=0
x=0
y=n-1
while i<=n-1:
    if a[i]<lv:
        a[i],a[x]=a[x],a[i]
        i=i+1
        x=x+1
    elif a[i]>hv:
        a[i],a[y]=a[y],a[i]
        y=y-1
    else:
        i=i+1
    if i==y:
        break
print(a)

#another approach#
'''a=[1,14,5,20,4,2,54,20,87,98,3,1,32]
lv=int(input("enter low value"))
hv=int(input("enter high value"))
n=len(a)
b=[]
c=[]
d=[]
for i in range(n):
    if a[i]<lv:
        b.append(a[i])
    if a[i]>hv:
        c.append(a[i])
    if a[i]>=lv and a[i]<=hv:
        d.append(a[i])
d.sort()
print(b+d+c)'''
        
