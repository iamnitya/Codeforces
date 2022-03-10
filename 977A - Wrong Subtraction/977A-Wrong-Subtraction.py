n=input()
n_s=n.split(" ")
x=int(n_s[0])
y=int(n_s[1])
for i in range(y):
    if x%10==0:
        x=int(x/10)
    else:
        x=x-1
print(x)
