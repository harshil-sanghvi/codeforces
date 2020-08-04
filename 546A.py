k,n,w=map(int,input().split(" "))

tot=0

for i in range(w):
    tot=tot+(i+1)*k
    i=i+1

tot = tot - n
if tot<0:
    tot=0

print(tot)