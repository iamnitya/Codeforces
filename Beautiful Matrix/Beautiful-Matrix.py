matrix=[]
for i in range(5):
    matrix.append(input().split())
    
row = 1
for i in matrix:
    if "1" in i:
        col = i.index('1')+1
        break
    row+=1
print(abs(row-3)+abs(col-3))
