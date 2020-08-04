n=int(input())

count=0
k=0

for i in range(n):
    s=input()
    k=0
    for j in s:
        if j=='1':
            k=k+1
    if k>1:
        count=count+1
    i=i+1


print(count)