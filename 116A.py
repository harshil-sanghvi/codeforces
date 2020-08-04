n=int(input())

present=0
capacity=0

for i in range(n):
    a , b = map(int,input().split(" "))
    present-=a
    present+=b
    capacity=max(present,capacity)

print(capacity)