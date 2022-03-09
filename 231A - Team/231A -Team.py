test_cases=int(input())
total=0
for i in range(test_cases):
    count=0
    l=input()
    k=l.split(" ")
    for j in range(len(k)):
        if int(k[j])==1:
            count+=1
    if count>=2:
        total+=1
print(total)
