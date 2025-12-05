n = int(input())
a= list(map(int, input().split()))
def ps(n,a):
    k = 0
    x = 0
    for i in range(1,n):
       h=0
       for j in range(n-1,0,-1):
            x+=1
            if a[j]<a[j-1]:
                a[j-1],a[j]=a[j],a[j-1]
                h+=1
                k+=1
       if h==0:
           break
    return k,x
print(ps(n,a))