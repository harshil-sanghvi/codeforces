n=int(input())

a=[]

for i in range(n):
    s=input()
    a.append(s)
    if len(a[i])>10:
        a[i]=s[0] + str(len(s)-2) + s[len(s)-1]
    i=i+1

for i in a:
    print(i)

