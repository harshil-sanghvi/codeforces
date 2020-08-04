k,n = map(int,input().split(" "))

for i in range(n):
    if k%10>0:
        k=k-1
    else:
        k=k/10
    i=i+1

print(int(k))