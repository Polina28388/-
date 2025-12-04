n = int(input())
a= list(map(int, input().split()))
k=0
x=0
for i in range(1,n):
    for j in range(n-1,0,-1):
        x+=1
        if a[j]<a[j-1]:
            a[j-1],a[j]=a[j],a[j-1]
            k+=1
print(*a,k,x)
