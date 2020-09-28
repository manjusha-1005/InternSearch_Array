a=[12,4,78,90,45,23]
n=len(a)
count=0
max=0
for i in range(n-1):
    if a[i]<a[i+1]:
        count=count+1
    else:
        if count>=1:
            if a[i+1]<a[i]:
                count=count+1
            else:
                continue
        else:
            continue
if count>max:
        max=count
print(max+1)
