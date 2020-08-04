numList = []
n,k = map(int,input().split(" "))
numList=list(map(int,input().split(" ")))

count=0

for i in numList:
    if i >= numList[k-1] and i>0:
        count=count+1

print(count)