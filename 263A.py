l=[]

for i in range(5):
    num=list(map(int,input().split(" ")))
    l.append(num)
    i=i+1

k=0
x=0
test=False

for i in l:
    k=k+1
    x=0
    for j in i:
        x=x+1
        if j==1:
            test=True
            break
    if test==True:
        break

print(abs(3-k)+abs(3-x))