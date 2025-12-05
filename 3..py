a=list(map(int, input().split()))
l=0
r=0
while l<r:
    for i in range(l,r):
        if a[i]>a[i+1]:
            a[i],a[i+1]=a[i+1],a[i]
    r-=1
    for j in range(r,l,-1):
        if a[j-1]>a[j]:
            a[j-1],a[j]=a[j],a[j-1]
    l+=1
print(*a)