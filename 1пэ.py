import random

def task1(k):
    min_sum = 1000000
    for i in range(0, len(k) - 1):
        s = k[i] + k[i + 1]
        if s <= min_sum:
            min_sum = s
            ind1 = i + 1
            ind2 = i + 2
    return ind1,ind2
print(task1([0,1,2,-2]))
def test_task1():
    if task1([0,1,2])==(1,2):
        print("+")
    else:
        print(f"error,для [0,1,2] ожидается:1,2, а у вас")
    if task1([0,2,3,6])==(1,2):
        print("+")
    else:
        print(f"error,для [0,2,3,6] ожидается:1,2, а у вас")
    if task1([2,5,3,4])==(3,4):
        print("+")
    else:
        print(f"error,для [2,5,1,6] ожидается:3,4, а у вас")
    if task1([1,4,5,2])==(1,2):
        print("+")
    else:
        print(f"error,для [1,4,5,2] ожидается:1,2, а у вас")
    if task1([4,2,6,5])==(1,2):
        print("+")
    else:
        print(f"error,для [4,2,6,5] ожидается:1,2, а у вас")
test_task1()
n=int(input())
k=[0]*n
a=int(input())
b=int(input())
for f in range(n):
    k[f]=random.randint(a,b)
print(k)
min_sum=1000000
for i in range(0,n-1):
    s=k[i]+k[i+1]
    if s<=min_sum:
        min_sum=s
        ind1=i+1
        ind2=i+2
print(ind1,ind2)