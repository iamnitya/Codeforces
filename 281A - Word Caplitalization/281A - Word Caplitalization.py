n=(input())
k=len(n)
l=[]
for j in range(k):
    p=n[j]
    l.append(p)
for i in range(len(l)):
    if i==0:
        p= l[i].upper()
        print(p,end="")
    else:
        p=l[i]
        print(p,end="")
