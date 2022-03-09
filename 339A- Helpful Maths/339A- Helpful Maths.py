s=input()
l=s.split("+")
l.sort()
if len(l)==1:
    print(l[0])
else:
    for i in range(len(l)-1):
        print(l[i],end='+')
    print(l[len(l)-1])
