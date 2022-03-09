t=input()
s=t.split(' ')
n=s[0]
k=s[1]
k_int=int(k)
l=input()
count=0
g=l.split(" ")
p=int(g[k_int-1])
for j in range(int(n)):
    if int(g[j])>=p and int(g[j])>0:
        count+=1
print(count)
