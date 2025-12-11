def task1(k):
    p=[]
    n=[]
    o=[]
    for i in range(0, len(k)):
        if k[i]>0:
            p.append(k[i])
        elif k[i]==0:
            n.append(k[i])
        else:
            o.append(k[i])
    s=p+n+o
    return s
print(task1([0,1,2,-2]))
def test_task1():
    if task1([0,1,2])==[1,2,0]:
        print("+")
    else:
        print(f"error,для [0,1,2] ожидается:1,2,0, а у вас")
    if task1([0,2,-3,6])==[2,6,0,-3]:
        print("+")
    else:
        print(f"error,для [0,2,-3,6] ожидается:2,6,0,-3, а у вас")
    if task1([2,-5,3,-4])==[2,3,-5,-4]:
        print("+")
    else:
        print(f"error,для [2,-5,3,-4] ожидается:2,3,-5,-4, а у вас")
    if task1([1,4,-5,-2])==[1,4,-5,-2]:
        print("+")
    else:
        print(f"error,для [1,4,-5,-2] ожидается:1,4,-5,-2, а у вас")
    if task1([0,-2,0,-5])==[0,0,-2,-5]:
        print("+")
    else:
        print(f"error,для [0,-2,0,-5] ожидается:0,0,-2,-5, а у вас")
test_task1()
k=list(map(int, input().split()))
p = []
n = []
o = []
for i in range(0, len(k)):
    if k[i] > 0:
        p.append(k[i])
    elif k[i] == 0:
        n.append(k[i])
    else:
        o.append(k[i])
s = p + n + o
print(s)