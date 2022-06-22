m = int(input())
x=0
for i in range(m):
    k = input()
    if k=="++X" or k=="X++":
        x=x+1
    if k=="--X" or k=="X--":
        x=x-1
print(x)
