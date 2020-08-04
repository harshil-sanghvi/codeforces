a,b=map(int,input().split(" "))

i=1
while i>=0:
    a*=3
    b*=2
    if a>b:
        print(i)
        break
    i=i+1
