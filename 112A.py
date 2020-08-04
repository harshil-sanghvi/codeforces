def compare(s1,s2):

    s1 = s1.upper()
    s2 = s2.upper()

    for i in range(len(s1)):
        if s1[i] < s2[i] :
            return -1
        elif s1[i] > s2[i]:
            return 1
    return 0

s1=input()
s2=input()

print(compare(s1,s2))