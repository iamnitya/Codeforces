n=input()
count_cap=0
count_small=0
capital=['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
for i in range(len(n)):
    if n[i] in capital:
        count_cap+=1
    else:
        count_small+=1
if count_cap>count_small:
    print(n.upper())
else:
    print(n.lower())
    
