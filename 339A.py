l=list(map(int,input().split("+")))

l.sort()
s=""
for i in l:
    # print(i)
    s=s+str(i)+"+"

s=s[:-1]
print(s)